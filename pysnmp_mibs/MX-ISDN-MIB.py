_q='physicalLinkInterfaceName'
_p='physicalLinkInfoInterfaceName'
_o='signalingChannelInteropInterfaceName'
_n='signalingChannelInfoInterfaceName'
_m='nationalStandard'
_l='isdnTelephony'
_k='abbreviated'
_j='subscriber'
_i='networkSpecific'
_h='national'
_g='explicit'
_f='automatic'
_e='transparent'
_d='sendAll'
_c='signalingChannelInterfaceName'
_b='bearerChannelInfoIndex'
_a='basicRateInterfaceInteropName'
_Z='deprecated'
_Y='basicRateInterfaceName'
_X='primaryRateInterfaceInteropName'
_W='enable'
_V='userOnly'
_U='roundRobinDescending'
_T='roundRobinAscending'
_S='descending'
_R='ascending'
_Q='transit'
_P='public'
_O='primaryRateInterfaceName'
_N='disable'
_M='unknown'
_L='g711ulaw'
_K='g711alaw'
_J='international'
_I='private'
_H='OctetString'
_G='MX-ISDN-MIB'
_F='Unsigned32'
_E='read-only'
_D='Integer32'
_C='MxEnableState'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_C,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
isdnMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850))
_IsdnMIBObjects_ObjectIdentity=ObjectIdentity
isdnMIBObjects=_IsdnMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1))
_PrimaryRateInterfaceGroup_ObjectIdentity=ObjectIdentity
primaryRateInterfaceGroup=_PrimaryRateInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200))
_PrimaryRateInterfaceTable_Object=MibTable
primaryRateInterfaceTable=_PrimaryRateInterfaceTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100))
if mibBuilder.loadTexts:primaryRateInterfaceTable.setStatus(_A)
_PrimaryRateInterfaceEntry_Object=MibTableRow
primaryRateInterfaceEntry=_PrimaryRateInterfaceEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1))
primaryRateInterfaceEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:primaryRateInterfaceEntry.setStatus(_A)
_PrimaryRateInterfaceName_Type=OctetString
_PrimaryRateInterfaceName_Object=MibTableColumn
primaryRateInterfaceName=_PrimaryRateInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,100),_PrimaryRateInterfaceName_Type())
primaryRateInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:primaryRateInterfaceName.setStatus(_A)
class _PrimaryRateInterfaceEndpointType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('te',100),('nt',200)))
_PrimaryRateInterfaceEndpointType_Type.__name__=_D
_PrimaryRateInterfaceEndpointType_Object=MibTableColumn
primaryRateInterfaceEndpointType=_PrimaryRateInterfaceEndpointType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,200),_PrimaryRateInterfaceEndpointType_Type())
primaryRateInterfaceEndpointType.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceEndpointType.setStatus(_A)
class _PrimaryRateInterfacePortPinout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('auto',100),('te',200),('nt',300)))
_PrimaryRateInterfacePortPinout_Type.__name__=_D
_PrimaryRateInterfacePortPinout_Object=MibTableColumn
primaryRateInterfacePortPinout=_PrimaryRateInterfacePortPinout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,250),_PrimaryRateInterfacePortPinout_Type())
primaryRateInterfacePortPinout.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfacePortPinout.setStatus(_A)
class _PrimaryRateInterfaceLineCoding_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('b8zs',100),('hdb3',200),('ami',300)))
_PrimaryRateInterfaceLineCoding_Type.__name__=_D
_PrimaryRateInterfaceLineCoding_Object=MibTableColumn
primaryRateInterfaceLineCoding=_PrimaryRateInterfaceLineCoding_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,400),_PrimaryRateInterfaceLineCoding_Type())
primaryRateInterfaceLineCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceLineCoding.setStatus(_A)
class _PrimaryRateInterfaceLineFraming_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sf',100),('esf',200),('crc4',300),('noCrc4',400)))
_PrimaryRateInterfaceLineFraming_Type.__name__=_D
_PrimaryRateInterfaceLineFraming_Object=MibTableColumn
primaryRateInterfaceLineFraming=_PrimaryRateInterfaceLineFraming_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,500),_PrimaryRateInterfaceLineFraming_Type())
primaryRateInterfaceLineFraming.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceLineFraming.setStatus(_A)
class _PrimaryRateInterfaceNetworkLocation_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('user',100),(_I,200),(_P,300),(_Q,400),(_J,500)))
_PrimaryRateInterfaceNetworkLocation_Type.__name__=_D
_PrimaryRateInterfaceNetworkLocation_Object=MibTableColumn
primaryRateInterfaceNetworkLocation=_PrimaryRateInterfaceNetworkLocation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,600),_PrimaryRateInterfaceNetworkLocation_Type())
primaryRateInterfaceNetworkLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceNetworkLocation.setStatus(_A)
class _PrimaryRateInterfacePreferredEncodingScheme_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),(_L,200)))
_PrimaryRateInterfacePreferredEncodingScheme_Type.__name__=_D
_PrimaryRateInterfacePreferredEncodingScheme_Object=MibTableColumn
primaryRateInterfacePreferredEncodingScheme=_PrimaryRateInterfacePreferredEncodingScheme_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,700),_PrimaryRateInterfacePreferredEncodingScheme_Type())
primaryRateInterfacePreferredEncodingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfacePreferredEncodingScheme.setStatus(_A)
class _PrimaryRateInterfaceFallbackEncodingScheme_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),(_L,200)))
_PrimaryRateInterfaceFallbackEncodingScheme_Type.__name__=_D
_PrimaryRateInterfaceFallbackEncodingScheme_Object=MibTableColumn
primaryRateInterfaceFallbackEncodingScheme=_PrimaryRateInterfaceFallbackEncodingScheme_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,750),_PrimaryRateInterfaceFallbackEncodingScheme_Type())
primaryRateInterfaceFallbackEncodingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceFallbackEncodingScheme.setStatus(_A)
class _PrimaryRateInterfaceChannelRange_Type(OctetString):defaultValue=OctetString('1-30');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_PrimaryRateInterfaceChannelRange_Type.__name__=_H
_PrimaryRateInterfaceChannelRange_Object=MibTableColumn
primaryRateInterfaceChannelRange=_PrimaryRateInterfaceChannelRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,800),_PrimaryRateInterfaceChannelRange_Type())
primaryRateInterfaceChannelRange.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceChannelRange.setStatus(_A)
class _PrimaryRateInterfaceIncomingChannelRange_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrimaryRateInterfaceIncomingChannelRange_Type.__name__=_H
_PrimaryRateInterfaceIncomingChannelRange_Object=MibTableColumn
primaryRateInterfaceIncomingChannelRange=_PrimaryRateInterfaceIncomingChannelRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,830),_PrimaryRateInterfaceIncomingChannelRange_Type())
primaryRateInterfaceIncomingChannelRange.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceIncomingChannelRange.setStatus(_A)
class _PrimaryRateInterfaceOutgoingChannelRange_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrimaryRateInterfaceOutgoingChannelRange_Type.__name__=_H
_PrimaryRateInterfaceOutgoingChannelRange_Object=MibTableColumn
primaryRateInterfaceOutgoingChannelRange=_PrimaryRateInterfaceOutgoingChannelRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,860),_PrimaryRateInterfaceOutgoingChannelRange_Type())
primaryRateInterfaceOutgoingChannelRange.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceOutgoingChannelRange.setStatus(_A)
class _PrimaryRateInterfaceChannelAllocationStrategy_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_R,100),(_S,200),(_T,300),(_U,400)))
_PrimaryRateInterfaceChannelAllocationStrategy_Type.__name__=_D
_PrimaryRateInterfaceChannelAllocationStrategy_Object=MibTableColumn
primaryRateInterfaceChannelAllocationStrategy=_PrimaryRateInterfaceChannelAllocationStrategy_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,900),_PrimaryRateInterfaceChannelAllocationStrategy_Type())
primaryRateInterfaceChannelAllocationStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceChannelAllocationStrategy.setStatus(_A)
class _PrimaryRateInterfaceMaxActiveCalls_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_PrimaryRateInterfaceMaxActiveCalls_Type.__name__=_F
_PrimaryRateInterfaceMaxActiveCalls_Object=MibTableColumn
primaryRateInterfaceMaxActiveCalls=_PrimaryRateInterfaceMaxActiveCalls_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1000),_PrimaryRateInterfaceMaxActiveCalls_Type())
primaryRateInterfaceMaxActiveCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceMaxActiveCalls.setStatus(_A)
class _PrimaryRateInterfaceSignalInformationElementEnable_Type(MxEnableState):defaultValue=0
_PrimaryRateInterfaceSignalInformationElementEnable_Type.__name__=_C
_PrimaryRateInterfaceSignalInformationElementEnable_Object=MibTableColumn
primaryRateInterfaceSignalInformationElementEnable=_PrimaryRateInterfaceSignalInformationElementEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1050),_PrimaryRateInterfaceSignalInformationElementEnable_Type())
primaryRateInterfaceSignalInformationElementEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceSignalInformationElementEnable.setStatus(_A)
class _PrimaryRateInterfaceInbandToneGenerationEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInbandToneGenerationEnable_Type.__name__=_C
_PrimaryRateInterfaceInbandToneGenerationEnable_Object=MibTableColumn
primaryRateInterfaceInbandToneGenerationEnable=_PrimaryRateInterfaceInbandToneGenerationEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1100),_PrimaryRateInterfaceInbandToneGenerationEnable_Type())
primaryRateInterfaceInbandToneGenerationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInbandToneGenerationEnable.setStatus(_A)
class _PrimaryRateInterfaceInbandDtmfDialingEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInbandDtmfDialingEnable_Type.__name__=_C
_PrimaryRateInterfaceInbandDtmfDialingEnable_Object=MibTableColumn
primaryRateInterfaceInbandDtmfDialingEnable=_PrimaryRateInterfaceInbandDtmfDialingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1200),_PrimaryRateInterfaceInbandDtmfDialingEnable_Type())
primaryRateInterfaceInbandDtmfDialingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInbandDtmfDialingEnable.setStatus(_A)
class _PrimaryRateInterfaceOverlapDialingEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceOverlapDialingEnable_Type.__name__=_C
_PrimaryRateInterfaceOverlapDialingEnable_Object=MibTableColumn
primaryRateInterfaceOverlapDialingEnable=_PrimaryRateInterfaceOverlapDialingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1300),_PrimaryRateInterfaceOverlapDialingEnable_Type())
primaryRateInterfaceOverlapDialingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceOverlapDialingEnable.setStatus(_A)
class _PrimaryRateInterfaceCallingNameMaxLength_Type(Unsigned32):defaultValue=34;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,82))
_PrimaryRateInterfaceCallingNameMaxLength_Type.__name__=_F
_PrimaryRateInterfaceCallingNameMaxLength_Object=MibTableColumn
primaryRateInterfaceCallingNameMaxLength=_PrimaryRateInterfaceCallingNameMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1400),_PrimaryRateInterfaceCallingNameMaxLength_Type())
primaryRateInterfaceCallingNameMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceCallingNameMaxLength.setStatus(_A)
class _PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Type(MxEnableState):defaultValue=0
_PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Type.__name__=_C
_PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Object=MibTableColumn
primaryRateInterfaceExclusiveBChannelSelectionEnable=_PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1500),_PrimaryRateInterfaceExclusiveBChannelSelectionEnable_Type())
primaryRateInterfaceExclusiveBChannelSelectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceExclusiveBChannelSelectionEnable.setStatus(_A)
class _PrimaryRateInterfaceSendingCompleteEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceSendingCompleteEnable_Type.__name__=_C
_PrimaryRateInterfaceSendingCompleteEnable_Object=MibTableColumn
primaryRateInterfaceSendingCompleteEnable=_PrimaryRateInterfaceSendingCompleteEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1600),_PrimaryRateInterfaceSendingCompleteEnable_Type())
primaryRateInterfaceSendingCompleteEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceSendingCompleteEnable.setStatus(_A)
class _PrimaryRateInterfaceClipEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_W,1),(_N,2)))
_PrimaryRateInterfaceClipEnable_Type.__name__=_D
_PrimaryRateInterfaceClipEnable_Object=MibTableColumn
primaryRateInterfaceClipEnable=_PrimaryRateInterfaceClipEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1700),_PrimaryRateInterfaceClipEnable_Type())
primaryRateInterfaceClipEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceClipEnable.setStatus(_A)
class _PrimaryRateInterfaceClirEnable_Type(MxEnableState):defaultValue=0
_PrimaryRateInterfaceClirEnable_Type.__name__=_C
_PrimaryRateInterfaceClirEnable_Object=MibTableColumn
primaryRateInterfaceClirEnable=_PrimaryRateInterfaceClirEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1725),_PrimaryRateInterfaceClirEnable_Type())
primaryRateInterfaceClirEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceClirEnable.setStatus(_A)
class _PrimaryRateInterfaceClirOverrideEnable_Type(MxEnableState):defaultValue=0
_PrimaryRateInterfaceClirOverrideEnable_Type.__name__=_C
_PrimaryRateInterfaceClirOverrideEnable_Object=MibTableColumn
primaryRateInterfaceClirOverrideEnable=_PrimaryRateInterfaceClirOverrideEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1750),_PrimaryRateInterfaceClirOverrideEnable_Type())
primaryRateInterfaceClirOverrideEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceClirOverrideEnable.setStatus(_A)
class _PrimaryRateInterfaceSendRestartOnStartupEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceSendRestartOnStartupEnable_Type.__name__=_C
_PrimaryRateInterfaceSendRestartOnStartupEnable_Object=MibTableColumn
primaryRateInterfaceSendRestartOnStartupEnable=_PrimaryRateInterfaceSendRestartOnStartupEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,100,1,1800),_PrimaryRateInterfaceSendRestartOnStartupEnable_Type())
primaryRateInterfaceSendRestartOnStartupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceSendRestartOnStartupEnable.setStatus(_A)
_PrimaryRateInterfaceInteropGroup_ObjectIdentity=ObjectIdentity
primaryRateInterfaceInteropGroup=_PrimaryRateInterfaceInteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000))
_PrimaryRateInterfaceInteropTable_Object=MibTable
primaryRateInterfaceInteropTable=_PrimaryRateInterfaceInteropTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100))
if mibBuilder.loadTexts:primaryRateInterfaceInteropTable.setStatus(_A)
_PrimaryRateInterfaceInteropEntry_Object=MibTableRow
primaryRateInterfaceInteropEntry=_PrimaryRateInterfaceInteropEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1))
primaryRateInterfaceInteropEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:primaryRateInterfaceInteropEntry.setStatus(_A)
_PrimaryRateInterfaceInteropName_Type=OctetString
_PrimaryRateInterfaceInteropName_Object=MibTableColumn
primaryRateInterfaceInteropName=_PrimaryRateInterfaceInteropName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,100),_PrimaryRateInterfaceInteropName_Type())
primaryRateInterfaceInteropName.setMaxAccess(_E)
if mibBuilder.loadTexts:primaryRateInterfaceInteropName.setStatus(_A)
class _PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Object=MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInSetupEnable=_PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,200),_PrimaryRateInterfaceInteropProgressIndicatorInSetupEnable_Type())
primaryRateInterfaceInteropProgressIndicatorInSetupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropProgressIndicatorInSetupEnable.setStatus(_A)
class _PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object=MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable=_PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,300),_PrimaryRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type())
primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable.setStatus(_A)
class _PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object=MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable=_PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,400),_PrimaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type())
primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setStatus(_A)
class _PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Object=MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInProgressEnable=_PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,450),_PrimaryRateInterfaceInteropProgressIndicatorInProgressEnable_Type())
primaryRateInterfaceInteropProgressIndicatorInProgressEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropProgressIndicatorInProgressEnable.setStatus(_A)
class _PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Object=MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInAlertingEnable=_PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,500),_PrimaryRateInterfaceInteropProgressIndicatorInAlertingEnable_Type())
primaryRateInterfaceInteropProgressIndicatorInAlertingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropProgressIndicatorInAlertingEnable.setStatus(_A)
class _PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Object=MibTableColumn
primaryRateInterfaceInteropProgressIndicatorInConnectEnable=_PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,600),_PrimaryRateInterfaceInteropProgressIndicatorInConnectEnable_Type())
primaryRateInterfaceInteropProgressIndicatorInConnectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropProgressIndicatorInConnectEnable.setStatus(_A)
class _PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Type.__name__=_F
_PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Object=MibTableColumn
primaryRateInterfaceInteropMaximumFacilityWaitingDelay=_PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,700),_PrimaryRateInterfaceInteropMaximumFacilityWaitingDelay_Type())
primaryRateInterfaceInteropMaximumFacilityWaitingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropMaximumFacilityWaitingDelay.setStatus(_A)
class _PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Type(MxEnableState):defaultValue=1
_PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Type.__name__=_C
_PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Object=MibTableColumn
primaryRateInterfaceInteropUseImplicitInbandInfoEnable=_PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,200,50000,100,1,800),_PrimaryRateInterfaceInteropUseImplicitInbandInfoEnable_Type())
primaryRateInterfaceInteropUseImplicitInbandInfoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryRateInterfaceInteropUseImplicitInbandInfoEnable.setStatus(_A)
_BasicRateInterfaceGroup_ObjectIdentity=ObjectIdentity
basicRateInterfaceGroup=_BasicRateInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300))
_BasicRateInterfaceTable_Object=MibTable
basicRateInterfaceTable=_BasicRateInterfaceTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100))
if mibBuilder.loadTexts:basicRateInterfaceTable.setStatus(_A)
_BasicRateInterfaceEntry_Object=MibTableRow
basicRateInterfaceEntry=_BasicRateInterfaceEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1))
basicRateInterfaceEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:basicRateInterfaceEntry.setStatus(_A)
_BasicRateInterfaceName_Type=OctetString
_BasicRateInterfaceName_Object=MibTableColumn
basicRateInterfaceName=_BasicRateInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,100),_BasicRateInterfaceName_Type())
basicRateInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:basicRateInterfaceName.setStatus(_A)
class _BasicRateInterfaceEndpointType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('te',100),('nt',200)))
_BasicRateInterfaceEndpointType_Type.__name__=_D
_BasicRateInterfaceEndpointType_Object=MibTableColumn
basicRateInterfaceEndpointType=_BasicRateInterfaceEndpointType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,200),_BasicRateInterfaceEndpointType_Type())
basicRateInterfaceEndpointType.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceEndpointType.setStatus(_A)
class _BasicRateInterfaceConnectionType_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('pointToPoint',100),('pointToMultiPoint',200)))
_BasicRateInterfaceConnectionType_Type.__name__=_D
_BasicRateInterfaceConnectionType_Object=MibTableColumn
basicRateInterfaceConnectionType=_BasicRateInterfaceConnectionType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,300),_BasicRateInterfaceConnectionType_Type())
basicRateInterfaceConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceConnectionType.setStatus(_A)
class _BasicRateInterfaceNetworkLocation_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('user',100),(_I,200),(_P,300),(_Q,400),(_J,500)))
_BasicRateInterfaceNetworkLocation_Type.__name__=_D
_BasicRateInterfaceNetworkLocation_Object=MibTableColumn
basicRateInterfaceNetworkLocation=_BasicRateInterfaceNetworkLocation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,600),_BasicRateInterfaceNetworkLocation_Type())
basicRateInterfaceNetworkLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceNetworkLocation.setStatus(_A)
class _BasicRateInterfacePreferredEncodingScheme_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),(_L,200)))
_BasicRateInterfacePreferredEncodingScheme_Type.__name__=_D
_BasicRateInterfacePreferredEncodingScheme_Object=MibTableColumn
basicRateInterfacePreferredEncodingScheme=_BasicRateInterfacePreferredEncodingScheme_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,700),_BasicRateInterfacePreferredEncodingScheme_Type())
basicRateInterfacePreferredEncodingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfacePreferredEncodingScheme.setStatus(_A)
class _BasicRateInterfaceFallbackEncodingScheme_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),(_L,200)))
_BasicRateInterfaceFallbackEncodingScheme_Type.__name__=_D
_BasicRateInterfaceFallbackEncodingScheme_Object=MibTableColumn
basicRateInterfaceFallbackEncodingScheme=_BasicRateInterfaceFallbackEncodingScheme_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,750),_BasicRateInterfaceFallbackEncodingScheme_Type())
basicRateInterfaceFallbackEncodingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceFallbackEncodingScheme.setStatus(_A)
class _BasicRateInterfaceChannelAllocationStrategy_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_R,100),(_S,200),(_T,300),(_U,400)))
_BasicRateInterfaceChannelAllocationStrategy_Type.__name__=_D
_BasicRateInterfaceChannelAllocationStrategy_Object=MibTableColumn
basicRateInterfaceChannelAllocationStrategy=_BasicRateInterfaceChannelAllocationStrategy_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,900),_BasicRateInterfaceChannelAllocationStrategy_Type())
basicRateInterfaceChannelAllocationStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceChannelAllocationStrategy.setStatus(_A)
class _BasicRateInterfaceMaxActiveCalls_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_BasicRateInterfaceMaxActiveCalls_Type.__name__=_F
_BasicRateInterfaceMaxActiveCalls_Object=MibTableColumn
basicRateInterfaceMaxActiveCalls=_BasicRateInterfaceMaxActiveCalls_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1000),_BasicRateInterfaceMaxActiveCalls_Type())
basicRateInterfaceMaxActiveCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceMaxActiveCalls.setStatus(_A)
class _BasicRateInterfaceSignalInformationElementEnable_Type(MxEnableState):defaultValue=0
_BasicRateInterfaceSignalInformationElementEnable_Type.__name__=_C
_BasicRateInterfaceSignalInformationElementEnable_Object=MibTableColumn
basicRateInterfaceSignalInformationElementEnable=_BasicRateInterfaceSignalInformationElementEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1050),_BasicRateInterfaceSignalInformationElementEnable_Type())
basicRateInterfaceSignalInformationElementEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceSignalInformationElementEnable.setStatus(_A)
class _BasicRateInterfaceInbandToneGenerationEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInbandToneGenerationEnable_Type.__name__=_C
_BasicRateInterfaceInbandToneGenerationEnable_Object=MibTableColumn
basicRateInterfaceInbandToneGenerationEnable=_BasicRateInterfaceInbandToneGenerationEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1100),_BasicRateInterfaceInbandToneGenerationEnable_Type())
basicRateInterfaceInbandToneGenerationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInbandToneGenerationEnable.setStatus(_A)
class _BasicRateInterfaceInbandDtmfDialingEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInbandDtmfDialingEnable_Type.__name__=_C
_BasicRateInterfaceInbandDtmfDialingEnable_Object=MibTableColumn
basicRateInterfaceInbandDtmfDialingEnable=_BasicRateInterfaceInbandDtmfDialingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1200),_BasicRateInterfaceInbandDtmfDialingEnable_Type())
basicRateInterfaceInbandDtmfDialingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInbandDtmfDialingEnable.setStatus(_A)
class _BasicRateInterfaceOverlapDialingEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceOverlapDialingEnable_Type.__name__=_C
_BasicRateInterfaceOverlapDialingEnable_Object=MibTableColumn
basicRateInterfaceOverlapDialingEnable=_BasicRateInterfaceOverlapDialingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1300),_BasicRateInterfaceOverlapDialingEnable_Type())
basicRateInterfaceOverlapDialingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceOverlapDialingEnable.setStatus(_A)
class _BasicRateInterfaceCallingNameMaxLength_Type(Unsigned32):defaultValue=34;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,82))
_BasicRateInterfaceCallingNameMaxLength_Type.__name__=_F
_BasicRateInterfaceCallingNameMaxLength_Object=MibTableColumn
basicRateInterfaceCallingNameMaxLength=_BasicRateInterfaceCallingNameMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1400),_BasicRateInterfaceCallingNameMaxLength_Type())
basicRateInterfaceCallingNameMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceCallingNameMaxLength.setStatus(_A)
class _BasicRateInterfaceExclusiveBChannelSelectionEnable_Type(MxEnableState):defaultValue=0
_BasicRateInterfaceExclusiveBChannelSelectionEnable_Type.__name__=_C
_BasicRateInterfaceExclusiveBChannelSelectionEnable_Object=MibTableColumn
basicRateInterfaceExclusiveBChannelSelectionEnable=_BasicRateInterfaceExclusiveBChannelSelectionEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1500),_BasicRateInterfaceExclusiveBChannelSelectionEnable_Type())
basicRateInterfaceExclusiveBChannelSelectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceExclusiveBChannelSelectionEnable.setStatus(_A)
class _BasicRateInterfaceSendingCompleteEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceSendingCompleteEnable_Type.__name__=_C
_BasicRateInterfaceSendingCompleteEnable_Object=MibTableColumn
basicRateInterfaceSendingCompleteEnable=_BasicRateInterfaceSendingCompleteEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1600),_BasicRateInterfaceSendingCompleteEnable_Type())
basicRateInterfaceSendingCompleteEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceSendingCompleteEnable.setStatus(_A)
class _BasicRateInterfaceClipEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_W,1),(_N,2)))
_BasicRateInterfaceClipEnable_Type.__name__=_D
_BasicRateInterfaceClipEnable_Object=MibTableColumn
basicRateInterfaceClipEnable=_BasicRateInterfaceClipEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1700),_BasicRateInterfaceClipEnable_Type())
basicRateInterfaceClipEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceClipEnable.setStatus(_A)
class _BasicRateInterfaceClirEnable_Type(MxEnableState):defaultValue=0
_BasicRateInterfaceClirEnable_Type.__name__=_C
_BasicRateInterfaceClirEnable_Object=MibTableColumn
basicRateInterfaceClirEnable=_BasicRateInterfaceClirEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1725),_BasicRateInterfaceClirEnable_Type())
basicRateInterfaceClirEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceClirEnable.setStatus(_A)
class _BasicRateInterfaceClirOverrideEnable_Type(MxEnableState):defaultValue=0
_BasicRateInterfaceClirOverrideEnable_Type.__name__=_C
_BasicRateInterfaceClirOverrideEnable_Object=MibTableColumn
basicRateInterfaceClirOverrideEnable=_BasicRateInterfaceClirOverrideEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1750),_BasicRateInterfaceClirOverrideEnable_Type())
basicRateInterfaceClirOverrideEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceClirOverrideEnable.setStatus(_A)
class _BasicRateInterfaceSendRestartOnStartupEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceSendRestartOnStartupEnable_Type.__name__=_C
_BasicRateInterfaceSendRestartOnStartupEnable_Object=MibTableColumn
basicRateInterfaceSendRestartOnStartupEnable=_BasicRateInterfaceSendRestartOnStartupEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1800),_BasicRateInterfaceSendRestartOnStartupEnable_Type())
basicRateInterfaceSendRestartOnStartupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceSendRestartOnStartupEnable.setStatus(_A)
class _BasicRateInterfaceHookFlashKeypad_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BasicRateInterfaceHookFlashKeypad_Type.__name__=_H
_BasicRateInterfaceHookFlashKeypad_Object=MibTableColumn
basicRateInterfaceHookFlashKeypad=_BasicRateInterfaceHookFlashKeypad_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,1900),_BasicRateInterfaceHookFlashKeypad_Type())
basicRateInterfaceHookFlashKeypad.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceHookFlashKeypad.setStatus(_A)
class _BasicRateInterfaceKeypadReceptionTimeout_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BasicRateInterfaceKeypadReceptionTimeout_Type.__name__=_F
_BasicRateInterfaceKeypadReceptionTimeout_Object=MibTableColumn
basicRateInterfaceKeypadReceptionTimeout=_BasicRateInterfaceKeypadReceptionTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,2000),_BasicRateInterfaceKeypadReceptionTimeout_Type())
basicRateInterfaceKeypadReceptionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceKeypadReceptionTimeout.setStatus(_A)
class _BasicRateInterfaceMsn_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BasicRateInterfaceMsn_Type.__name__=_H
_BasicRateInterfaceMsn_Object=MibTableColumn
basicRateInterfaceMsn=_BasicRateInterfaceMsn_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,2200),_BasicRateInterfaceMsn_Type())
basicRateInterfaceMsn.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceMsn.setStatus(_A)
class _BasicRateInterfaceMsn2_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BasicRateInterfaceMsn2_Type.__name__=_H
_BasicRateInterfaceMsn2_Object=MibTableColumn
basicRateInterfaceMsn2=_BasicRateInterfaceMsn2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,2300),_BasicRateInterfaceMsn2_Type())
basicRateInterfaceMsn2.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceMsn2.setStatus(_Z)
class _BasicRateInterfaceMsn3_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BasicRateInterfaceMsn3_Type.__name__=_H
_BasicRateInterfaceMsn3_Object=MibTableColumn
basicRateInterfaceMsn3=_BasicRateInterfaceMsn3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,2400),_BasicRateInterfaceMsn3_Type())
basicRateInterfaceMsn3.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceMsn3.setStatus(_Z)
class _BasicRateInterfaceTeiNegotiation_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('linkUp',100),('powerUp',200),('signalingUp',300)))
_BasicRateInterfaceTeiNegotiation_Type.__name__=_D
_BasicRateInterfaceTeiNegotiation_Object=MibTableColumn
basicRateInterfaceTeiNegotiation=_BasicRateInterfaceTeiNegotiation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,100,1,2500),_BasicRateInterfaceTeiNegotiation_Type())
basicRateInterfaceTeiNegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceTeiNegotiation.setStatus(_A)
_BasicRateInterfaceInteropGroup_ObjectIdentity=ObjectIdentity
basicRateInterfaceInteropGroup=_BasicRateInterfaceInteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000))
_BasicRateInterfaceInteropTable_Object=MibTable
basicRateInterfaceInteropTable=_BasicRateInterfaceInteropTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100))
if mibBuilder.loadTexts:basicRateInterfaceInteropTable.setStatus(_A)
_BasicRateInterfaceInteropEntry_Object=MibTableRow
basicRateInterfaceInteropEntry=_BasicRateInterfaceInteropEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1))
basicRateInterfaceInteropEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:basicRateInterfaceInteropEntry.setStatus(_A)
_BasicRateInterfaceInteropName_Type=OctetString
_BasicRateInterfaceInteropName_Object=MibTableColumn
basicRateInterfaceInteropName=_BasicRateInterfaceInteropName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,100),_BasicRateInterfaceInteropName_Type())
basicRateInterfaceInteropName.setMaxAccess(_E)
if mibBuilder.loadTexts:basicRateInterfaceInteropName.setStatus(_A)
class _BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Type.__name__=_C
_BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Object=MibTableColumn
basicRateInterfaceInteropProgressIndicatorInSetupEnable=_BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,200),_BasicRateInterfaceInteropProgressIndicatorInSetupEnable_Type())
basicRateInterfaceInteropProgressIndicatorInSetupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropProgressIndicatorInSetupEnable.setStatus(_A)
class _BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type.__name__=_C
_BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object=MibTableColumn
basicRateInterfaceInteropProgressIndicatorInSetupAckEnable=_BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,300),_BasicRateInterfaceInteropProgressIndicatorInSetupAckEnable_Type())
basicRateInterfaceInteropProgressIndicatorInSetupAckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropProgressIndicatorInSetupAckEnable.setStatus(_A)
class _BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type.__name__=_C
_BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object=MibTableColumn
basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable=_BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,400),_BasicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable_Type())
basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable.setStatus(_A)
class _BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Type.__name__=_C
_BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Object=MibTableColumn
basicRateInterfaceInteropProgressIndicatorInProgressEnable=_BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,450),_BasicRateInterfaceInteropProgressIndicatorInProgressEnable_Type())
basicRateInterfaceInteropProgressIndicatorInProgressEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropProgressIndicatorInProgressEnable.setStatus(_A)
class _BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Type.__name__=_C
_BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Object=MibTableColumn
basicRateInterfaceInteropProgressIndicatorInAlertingEnable=_BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,500),_BasicRateInterfaceInteropProgressIndicatorInAlertingEnable_Type())
basicRateInterfaceInteropProgressIndicatorInAlertingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropProgressIndicatorInAlertingEnable.setStatus(_A)
class _BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Type.__name__=_C
_BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Object=MibTableColumn
basicRateInterfaceInteropProgressIndicatorInConnectEnable=_BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,600),_BasicRateInterfaceInteropProgressIndicatorInConnectEnable_Type())
basicRateInterfaceInteropProgressIndicatorInConnectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropProgressIndicatorInConnectEnable.setStatus(_A)
class _BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Type.__name__=_F
_BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Object=MibTableColumn
basicRateInterfaceInteropMaximumFacilityWaitingDelay=_BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,700),_BasicRateInterfaceInteropMaximumFacilityWaitingDelay_Type())
basicRateInterfaceInteropMaximumFacilityWaitingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropMaximumFacilityWaitingDelay.setStatus(_A)
class _BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Type.__name__=_C
_BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Object=MibTableColumn
basicRateInterfaceInteropUseImplicitInbandInfoEnable=_BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,800),_BasicRateInterfaceInteropUseImplicitInbandInfoEnable_Type())
basicRateInterfaceInteropUseImplicitInbandInfoEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropUseImplicitInbandInfoEnable.setStatus(_A)
class _BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Type(MxEnableState):defaultValue=1
_BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Type.__name__=_C
_BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Object=MibTableColumn
basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable=_BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,300,50000,100,1,900),_BasicRateInterfaceInteropAllowTeiBroadcastInPtpEnable_Type())
basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable.setStatus(_A)
_BearerChannelGroup_ObjectIdentity=ObjectIdentity
bearerChannelGroup=_BearerChannelGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,400))
_BearerChannelInfoTable_Object=MibTable
bearerChannelInfoTable=_BearerChannelInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,400,100))
if mibBuilder.loadTexts:bearerChannelInfoTable.setStatus(_A)
_BearerChannelInfoEntry_Object=MibTableRow
bearerChannelInfoEntry=_BearerChannelInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,400,100,1))
bearerChannelInfoEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:bearerChannelInfoEntry.setStatus(_A)
_BearerChannelInfoIndex_Type=OctetString
_BearerChannelInfoIndex_Object=MibTableColumn
bearerChannelInfoIndex=_BearerChannelInfoIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,400,100,1,100),_BearerChannelInfoIndex_Type())
bearerChannelInfoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bearerChannelInfoIndex.setStatus(_A)
class _BearerChannelInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('idle',100),('inUse',200),('maintenance',300),('error',400),('disabled',500)))
_BearerChannelInfoState_Type.__name__=_D
_BearerChannelInfoState_Object=MibTableColumn
bearerChannelInfoState=_BearerChannelInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,400,100,1,200),_BearerChannelInfoState_Type())
bearerChannelInfoState.setMaxAccess(_E)
if mibBuilder.loadTexts:bearerChannelInfoState.setStatus(_A)
_SignalingChannelGroup_ObjectIdentity=ObjectIdentity
signalingChannelGroup=_SignalingChannelGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500))
_SignalingChannelTable_Object=MibTable
signalingChannelTable=_SignalingChannelTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100))
if mibBuilder.loadTexts:signalingChannelTable.setStatus(_A)
_SignalingChannelEntry_Object=MibTableRow
signalingChannelEntry=_SignalingChannelEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1))
signalingChannelEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:signalingChannelEntry.setStatus(_A)
_SignalingChannelInterfaceName_Type=OctetString
_SignalingChannelInterfaceName_Object=MibTableColumn
signalingChannelInterfaceName=_SignalingChannelInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,100),_SignalingChannelInterfaceName_Type())
signalingChannelInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:signalingChannelInterfaceName.setStatus(_A)
class _SignalingChannelProtocol_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('dss1',100),('dms100',200),('ni2',300),('ess5',400),('qSig',500)))
_SignalingChannelProtocol_Type.__name__=_D
_SignalingChannelProtocol_Object=MibTableColumn
signalingChannelProtocol=_SignalingChannelProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,200),_SignalingChannelProtocol_Type())
signalingChannelProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelProtocol.setStatus(_A)
class _SignalingChannelFacilityServicesEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelFacilityServicesEnable_Type.__name__=_C
_SignalingChannelFacilityServicesEnable_Object=MibTableColumn
signalingChannelFacilityServicesEnable=_SignalingChannelFacilityServicesEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,250),_SignalingChannelFacilityServicesEnable_Type())
signalingChannelFacilityServicesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelFacilityServicesEnable.setStatus(_A)
class _SignalingChannelColpEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelColpEnable_Type.__name__=_C
_SignalingChannelColpEnable_Object=MibTableColumn
signalingChannelColpEnable=_SignalingChannelColpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,300),_SignalingChannelColpEnable_Type())
signalingChannelColpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelColpEnable.setStatus(_A)
class _SignalingChannelColrEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelColrEnable_Type.__name__=_C
_SignalingChannelColrEnable_Object=MibTableColumn
signalingChannelColrEnable=_SignalingChannelColrEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,400),_SignalingChannelColrEnable_Type())
signalingChannelColrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelColrEnable.setStatus(_A)
class _SignalingChannelColrOverrideEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelColrOverrideEnable_Type.__name__=_C
_SignalingChannelColrOverrideEnable_Object=MibTableColumn
signalingChannelColrOverrideEnable=_SignalingChannelColrOverrideEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,500),_SignalingChannelColrOverrideEnable_Type())
signalingChannelColrOverrideEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelColrOverrideEnable.setStatus(_A)
class _SignalingChannelConpEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelConpEnable_Type.__name__=_C
_SignalingChannelConpEnable_Object=MibTableColumn
signalingChannelConpEnable=_SignalingChannelConpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,510),_SignalingChannelConpEnable_Type())
signalingChannelConpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelConpEnable.setStatus(_A)
class _SignalingChannelOutgoingNotifyEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelOutgoingNotifyEnable_Type.__name__=_C
_SignalingChannelOutgoingNotifyEnable_Object=MibTableColumn
signalingChannelOutgoingNotifyEnable=_SignalingChannelOutgoingNotifyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,600),_SignalingChannelOutgoingNotifyEnable_Type())
signalingChannelOutgoingNotifyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelOutgoingNotifyEnable.setStatus(_A)
class _SignalingChannelAcceptedProgressCauses_Type(OctetString):defaultValue=OctetString('1-127');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SignalingChannelAcceptedProgressCauses_Type.__name__=_H
_SignalingChannelAcceptedProgressCauses_Object=MibTableColumn
signalingChannelAcceptedProgressCauses=_SignalingChannelAcceptedProgressCauses_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,700),_SignalingChannelAcceptedProgressCauses_Type())
signalingChannelAcceptedProgressCauses.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelAcceptedProgressCauses.setStatus(_A)
class _SignalingChannelAutoCancelTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_SignalingChannelAutoCancelTimeout_Type.__name__=_F
_SignalingChannelAutoCancelTimeout_Object=MibTableColumn
signalingChannelAutoCancelTimeout=_SignalingChannelAutoCancelTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,800),_SignalingChannelAutoCancelTimeout_Type())
signalingChannelAutoCancelTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelAutoCancelTimeout.setStatus(_A)
class _SignalingChannelDateTimeIeSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('none',100),('localTime',200),('utc',300)))
_SignalingChannelDateTimeIeSupport_Type.__name__=_D
_SignalingChannelDateTimeIeSupport_Object=MibTableColumn
signalingChannelDateTimeIeSupport=_SignalingChannelDateTimeIeSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,900),_SignalingChannelDateTimeIeSupport_Type())
signalingChannelDateTimeIeSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDateTimeIeSupport.setStatus(_A)
class _SignalingChannelMaintenanceServiceCallTermination_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('graceful',100),('abrupt',200)))
_SignalingChannelMaintenanceServiceCallTermination_Type.__name__=_D
_SignalingChannelMaintenanceServiceCallTermination_Object=MibTableColumn
signalingChannelMaintenanceServiceCallTermination=_SignalingChannelMaintenanceServiceCallTermination_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10000),_SignalingChannelMaintenanceServiceCallTermination_Type())
signalingChannelMaintenanceServiceCallTermination.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelMaintenanceServiceCallTermination.setStatus(_A)
class _SignalingChannelLinkEstablishment_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('onDemand',100),('permanent',200)))
_SignalingChannelLinkEstablishment_Type.__name__=_D
_SignalingChannelLinkEstablishment_Object=MibTableColumn
signalingChannelLinkEstablishment=_SignalingChannelLinkEstablishment_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10100),_SignalingChannelLinkEstablishment_Type())
signalingChannelLinkEstablishment.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelLinkEstablishment.setStatus(_A)
class _SignalingChannelLinkEstablishmentTimer_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_SignalingChannelLinkEstablishmentTimer_Type.__name__=_F
_SignalingChannelLinkEstablishmentTimer_Object=MibTableColumn
signalingChannelLinkEstablishmentTimer=_SignalingChannelLinkEstablishmentTimer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10110),_SignalingChannelLinkEstablishmentTimer_Type())
signalingChannelLinkEstablishmentTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelLinkEstablishmentTimer.setStatus(_A)
class _SignalingChannelAcceptedStatusCauses_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SignalingChannelAcceptedStatusCauses_Type.__name__=_H
_SignalingChannelAcceptedStatusCauses_Object=MibTableColumn
signalingChannelAcceptedStatusCauses=_SignalingChannelAcceptedStatusCauses_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10200),_SignalingChannelAcceptedStatusCauses_Type())
signalingChannelAcceptedStatusCauses.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelAcceptedStatusCauses.setStatus(_A)
class _SignalingChannelSendIsdnProgress_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_d,100),('sendInband',200),('sendAlerting',300)))
_SignalingChannelSendIsdnProgress_Type.__name__=_D
_SignalingChannelSendIsdnProgress_Object=MibTableColumn
signalingChannelSendIsdnProgress=_SignalingChannelSendIsdnProgress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10300),_SignalingChannelSendIsdnProgress_Type())
signalingChannelSendIsdnProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelSendIsdnProgress.setStatus(_A)
class _SignalingChannelSendProgressIndicatorIE_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_d,100),('sendInbandOnly',200)))
_SignalingChannelSendProgressIndicatorIE_Type.__name__=_D
_SignalingChannelSendProgressIndicatorIE_Object=MibTableColumn
signalingChannelSendProgressIndicatorIE=_SignalingChannelSendProgressIndicatorIE_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10400),_SignalingChannelSendProgressIndicatorIE_Type())
signalingChannelSendProgressIndicatorIE.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelSendProgressIndicatorIE.setStatus(_A)
class _SignalingChannelAocESupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('no',100),(_e,200),(_f,300),(_g,400)))
_SignalingChannelAocESupport_Type.__name__=_D
_SignalingChannelAocESupport_Object=MibTableColumn
signalingChannelAocESupport=_SignalingChannelAocESupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10600),_SignalingChannelAocESupport_Type())
signalingChannelAocESupport.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelAocESupport.setStatus(_A)
class _SignalingChannelAocDSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('no',100),(_e,200),(_f,300),(_g,400)))
_SignalingChannelAocDSupport_Type.__name__=_D
_SignalingChannelAocDSupport_Object=MibTableColumn
signalingChannelAocDSupport=_SignalingChannelAocDSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10620),_SignalingChannelAocDSupport_Type())
signalingChannelAocDSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelAocDSupport.setStatus(_A)
class _SignalingChannelCallReroutingBehavior_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('unsupported',100),('relayReroute',200),('processLocally',300)))
_SignalingChannelCallReroutingBehavior_Type.__name__=_D
_SignalingChannelCallReroutingBehavior_Object=MibTableColumn
signalingChannelCallReroutingBehavior=_SignalingChannelCallReroutingBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10700),_SignalingChannelCallReroutingBehavior_Type())
signalingChannelCallReroutingBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelCallReroutingBehavior.setStatus(_A)
class _SignalingChannelDefaultCallingTon_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*((_M,100),(_J,200),(_h,300),(_i,400),(_j,500),(_k,600)))
_SignalingChannelDefaultCallingTon_Type.__name__=_D
_SignalingChannelDefaultCallingTon_Object=MibTableColumn
signalingChannelDefaultCallingTon=_SignalingChannelDefaultCallingTon_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10800),_SignalingChannelDefaultCallingTon_Type())
signalingChannelDefaultCallingTon.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDefaultCallingTon.setStatus(_A)
class _SignalingChannelDefaultCallingNpi_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*((_M,100),(_l,200),('data',300),('telex',400),(_m,500),(_I,600)))
_SignalingChannelDefaultCallingNpi_Type.__name__=_D
_SignalingChannelDefaultCallingNpi_Object=MibTableColumn
signalingChannelDefaultCallingNpi=_SignalingChannelDefaultCallingNpi_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,10900),_SignalingChannelDefaultCallingNpi_Type())
signalingChannelDefaultCallingNpi.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDefaultCallingNpi.setStatus(_A)
class _SignalingChannelDefaultCallingPi_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('presentationAllowed',100),('presentationRestricted',200),('notAvailable',300)))
_SignalingChannelDefaultCallingPi_Type.__name__=_D
_SignalingChannelDefaultCallingPi_Object=MibTableColumn
signalingChannelDefaultCallingPi=_SignalingChannelDefaultCallingPi_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11000),_SignalingChannelDefaultCallingPi_Type())
signalingChannelDefaultCallingPi.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDefaultCallingPi.setStatus(_A)
class _SignalingChannelDefaultCallingSi_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('userProvidedNotScreened',100),('userProvidedVerifiedAndPassed',200),('userProvidedVerifiedAndFailed',300),('networkProvided',400),('contextDependent',500)))
_SignalingChannelDefaultCallingSi_Type.__name__=_D
_SignalingChannelDefaultCallingSi_Object=MibTableColumn
signalingChannelDefaultCallingSi=_SignalingChannelDefaultCallingSi_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11100),_SignalingChannelDefaultCallingSi_Type())
signalingChannelDefaultCallingSi.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDefaultCallingSi.setStatus(_A)
class _SignalingChannelDefaultCalledTon_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*((_M,100),(_J,200),(_h,300),(_i,400),(_j,500),(_k,600)))
_SignalingChannelDefaultCalledTon_Type.__name__=_D
_SignalingChannelDefaultCalledTon_Object=MibTableColumn
signalingChannelDefaultCalledTon=_SignalingChannelDefaultCalledTon_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11200),_SignalingChannelDefaultCalledTon_Type())
signalingChannelDefaultCalledTon.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDefaultCalledTon.setStatus(_A)
class _SignalingChannelDefaultCalledNpi_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*((_M,100),(_l,200),('data',300),('telex',400),(_m,500),(_I,600)))
_SignalingChannelDefaultCalledNpi_Type.__name__=_D
_SignalingChannelDefaultCalledNpi_Object=MibTableColumn
signalingChannelDefaultCalledNpi=_SignalingChannelDefaultCalledNpi_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11300),_SignalingChannelDefaultCalledNpi_Type())
signalingChannelDefaultCalledNpi.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelDefaultCalledNpi.setStatus(_A)
class _SignalingChannelUserSuspendedHandling_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('ignore',100),('disconnect',200)))
_SignalingChannelUserSuspendedHandling_Type.__name__=_D
_SignalingChannelUserSuspendedHandling_Object=MibTableColumn
signalingChannelUserSuspendedHandling=_SignalingChannelUserSuspendedHandling_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11400),_SignalingChannelUserSuspendedHandling_Type())
signalingChannelUserSuspendedHandling.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelUserSuspendedHandling.setStatus(_A)
class _SignalingChannelStrictHandlingErrorConditions_Type(MxEnableState):defaultValue=0
_SignalingChannelStrictHandlingErrorConditions_Type.__name__=_C
_SignalingChannelStrictHandlingErrorConditions_Object=MibTableColumn
signalingChannelStrictHandlingErrorConditions=_SignalingChannelStrictHandlingErrorConditions_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11500),_SignalingChannelStrictHandlingErrorConditions_Type())
signalingChannelStrictHandlingErrorConditions.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelStrictHandlingErrorConditions.setStatus(_A)
class _SignalingChannelMcidEnable_Type(MxEnableState):defaultValue=0
_SignalingChannelMcidEnable_Type.__name__=_C
_SignalingChannelMcidEnable_Object=MibTableColumn
signalingChannelMcidEnable=_SignalingChannelMcidEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,100,1,11600),_SignalingChannelMcidEnable_Type())
signalingChannelMcidEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelMcidEnable.setStatus(_A)
_SignalingChannelInfoTable_Object=MibTable
signalingChannelInfoTable=_SignalingChannelInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,200))
if mibBuilder.loadTexts:signalingChannelInfoTable.setStatus(_A)
_SignalingChannelInfoEntry_Object=MibTableRow
signalingChannelInfoEntry=_SignalingChannelInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,200,1))
signalingChannelInfoEntry.setIndexNames((0,_G,_n))
if mibBuilder.loadTexts:signalingChannelInfoEntry.setStatus(_A)
_SignalingChannelInfoInterfaceName_Type=OctetString
_SignalingChannelInfoInterfaceName_Object=MibTableColumn
signalingChannelInfoInterfaceName=_SignalingChannelInfoInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,200,1,100),_SignalingChannelInfoInterfaceName_Type())
signalingChannelInfoInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:signalingChannelInfoInterfaceName.setStatus(_A)
class _SignalingChannelInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('up',100),('down',200)))
_SignalingChannelInfoState_Type.__name__=_D
_SignalingChannelInfoState_Object=MibTableColumn
signalingChannelInfoState=_SignalingChannelInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,200,1,200),_SignalingChannelInfoState_Type())
signalingChannelInfoState.setMaxAccess(_E)
if mibBuilder.loadTexts:signalingChannelInfoState.setStatus(_A)
_SignalingChannelInteropGroup_ObjectIdentity=ObjectIdentity
signalingChannelInteropGroup=_SignalingChannelInteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000))
_SignalingChannelInteropTable_Object=MibTable
signalingChannelInteropTable=_SignalingChannelInteropTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100))
if mibBuilder.loadTexts:signalingChannelInteropTable.setStatus(_A)
_SignalingChannelInteropEntry_Object=MibTableRow
signalingChannelInteropEntry=_SignalingChannelInteropEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1))
signalingChannelInteropEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:signalingChannelInteropEntry.setStatus(_A)
_SignalingChannelInteropInterfaceName_Type=OctetString
_SignalingChannelInteropInterfaceName_Object=MibTableColumn
signalingChannelInteropInterfaceName=_SignalingChannelInteropInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1,100),_SignalingChannelInteropInterfaceName_Type())
signalingChannelInteropInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:signalingChannelInteropInterfaceName.setStatus(_A)
class _SignalingChannelInteropCallProceedingDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_SignalingChannelInteropCallProceedingDelay_Type.__name__=_F
_SignalingChannelInteropCallProceedingDelay_Object=MibTableColumn
signalingChannelInteropCallProceedingDelay=_SignalingChannelInteropCallProceedingDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1,200),_SignalingChannelInteropCallProceedingDelay_Type())
signalingChannelInteropCallProceedingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelInteropCallProceedingDelay.setStatus(_A)
class _SignalingChannelInteropCallingNameDelivery_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('facilityIe',100),('displayIe',200),('userUserIe',300),('signalingProtocol',400)))
_SignalingChannelInteropCallingNameDelivery_Type.__name__=_D
_SignalingChannelInteropCallingNameDelivery_Object=MibTableColumn
signalingChannelInteropCallingNameDelivery=_SignalingChannelInteropCallingNameDelivery_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1,300),_SignalingChannelInteropCallingNameDelivery_Type())
signalingChannelInteropCallingNameDelivery.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelInteropCallingNameDelivery.setStatus(_A)
class _SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Type(MxEnableState):defaultValue=0
_SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Type.__name__=_C
_SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Object=MibTableColumn
signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream=_SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1,500),_SignalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream_Type())
signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream.setStatus(_A)
class _SignalingChannelInteropInteropConsecutiveChannelIndicator_Type(MxEnableState):defaultValue=0
_SignalingChannelInteropInteropConsecutiveChannelIndicator_Type.__name__=_C
_SignalingChannelInteropInteropConsecutiveChannelIndicator_Object=MibTableColumn
signalingChannelInteropInteropConsecutiveChannelIndicator=_SignalingChannelInteropInteropConsecutiveChannelIndicator_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1,600),_SignalingChannelInteropInteropConsecutiveChannelIndicator_Type())
signalingChannelInteropInteropConsecutiveChannelIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelInteropInteropConsecutiveChannelIndicator.setStatus(_A)
class _SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Type(MxEnableState):defaultValue=1
_SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Type.__name__=_C
_SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Object=MibTableColumn
signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry=_SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,500,50000,100,1,700),_SignalingChannelInteropInteropAddReleaseSecondCauseOnExpiry_Type())
signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry.setStatus(_A)
_PhysicalGroup_ObjectIdentity=ObjectIdentity
physicalGroup=_PhysicalGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600))
_PhysicalLinkInfoTable_Object=MibTable
physicalLinkInfoTable=_PhysicalLinkInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,100))
if mibBuilder.loadTexts:physicalLinkInfoTable.setStatus(_A)
_PhysicalLinkInfoEntry_Object=MibTableRow
physicalLinkInfoEntry=_PhysicalLinkInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,100,1))
physicalLinkInfoEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:physicalLinkInfoEntry.setStatus(_A)
_PhysicalLinkInfoInterfaceName_Type=OctetString
_PhysicalLinkInfoInterfaceName_Object=MibTableColumn
physicalLinkInfoInterfaceName=_PhysicalLinkInfoInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,100,1,100),_PhysicalLinkInfoInterfaceName_Type())
physicalLinkInfoInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:physicalLinkInfoInterfaceName.setStatus(_A)
class _PhysicalLinkInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('up',100),('down',200)))
_PhysicalLinkInfoState_Type.__name__=_D
_PhysicalLinkInfoState_Object=MibTableColumn
physicalLinkInfoState=_PhysicalLinkInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,100,1,200),_PhysicalLinkInfoState_Type())
physicalLinkInfoState.setMaxAccess(_E)
if mibBuilder.loadTexts:physicalLinkInfoState.setStatus(_A)
_PhysicalLinkTable_Object=MibTable
physicalLinkTable=_PhysicalLinkTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,200))
if mibBuilder.loadTexts:physicalLinkTable.setStatus(_A)
_PhysicalLinkEntry_Object=MibTableRow
physicalLinkEntry=_PhysicalLinkEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,200,1))
physicalLinkEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:physicalLinkEntry.setStatus(_A)
_PhysicalLinkInterfaceName_Type=OctetString
_PhysicalLinkInterfaceName_Object=MibTableColumn
physicalLinkInterfaceName=_PhysicalLinkInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,200,1,100),_PhysicalLinkInterfaceName_Type())
physicalLinkInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:physicalLinkInterfaceName.setStatus(_A)
class _PhysicalLinkL1TimerT3_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_PhysicalLinkL1TimerT3_Type.__name__=_F
_PhysicalLinkL1TimerT3_Object=MibTableColumn
physicalLinkL1TimerT3=_PhysicalLinkL1TimerT3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,200,1,200),_PhysicalLinkL1TimerT3_Type())
physicalLinkL1TimerT3.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkL1TimerT3.setStatus(_A)
class _PhysicalLinkClockMode_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('auto',100),('master',200),('slave',300)))
_PhysicalLinkClockMode_Type.__name__=_D
_PhysicalLinkClockMode_Object=MibTableColumn
physicalLinkClockMode=_PhysicalLinkClockMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,200,1,300),_PhysicalLinkClockMode_Type())
physicalLinkClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkClockMode.setStatus(_A)
class _PhysicalLinkMonitorLinkStateEnable_Type(MxEnableState):defaultValue=1
_PhysicalLinkMonitorLinkStateEnable_Type.__name__=_C
_PhysicalLinkMonitorLinkStateEnable_Object=MibTableColumn
physicalLinkMonitorLinkStateEnable=_PhysicalLinkMonitorLinkStateEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,600,200,1,400),_PhysicalLinkMonitorLinkStateEnable_Type())
physicalLinkMonitorLinkStateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkMonitorLinkStateEnable.setStatus(_A)
_AutoConfigure_ObjectIdentity=ObjectIdentity
autoConfigure=_AutoConfigure_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,700))
class _AutoConfigureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('idle',100),('sensing',200)))
_AutoConfigureStatus_Type.__name__=_D
_AutoConfigureStatus_Object=MibScalar
autoConfigureStatus=_AutoConfigureStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,700,100),_AutoConfigureStatus_Type())
autoConfigureStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:autoConfigureStatus.setStatus(_A)
class _LastAutoConfigureResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('none',100),('success',200),('fail',300),('aborted',400)))
_LastAutoConfigureResult_Type.__name__=_D
_LastAutoConfigureResult_Object=MibScalar
lastAutoConfigureResult=_LastAutoConfigureResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,700,200),_LastAutoConfigureResult_Type())
lastAutoConfigureResult.setMaxAccess(_E)
if mibBuilder.loadTexts:lastAutoConfigureResult.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_N,0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1850,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'isdnMIB':isdnMIB,'isdnMIBObjects':isdnMIBObjects,'primaryRateInterfaceGroup':primaryRateInterfaceGroup,'primaryRateInterfaceTable':primaryRateInterfaceTable,'primaryRateInterfaceEntry':primaryRateInterfaceEntry,_O:primaryRateInterfaceName,'primaryRateInterfaceEndpointType':primaryRateInterfaceEndpointType,'primaryRateInterfacePortPinout':primaryRateInterfacePortPinout,'primaryRateInterfaceLineCoding':primaryRateInterfaceLineCoding,'primaryRateInterfaceLineFraming':primaryRateInterfaceLineFraming,'primaryRateInterfaceNetworkLocation':primaryRateInterfaceNetworkLocation,'primaryRateInterfacePreferredEncodingScheme':primaryRateInterfacePreferredEncodingScheme,'primaryRateInterfaceFallbackEncodingScheme':primaryRateInterfaceFallbackEncodingScheme,'primaryRateInterfaceChannelRange':primaryRateInterfaceChannelRange,'primaryRateInterfaceIncomingChannelRange':primaryRateInterfaceIncomingChannelRange,'primaryRateInterfaceOutgoingChannelRange':primaryRateInterfaceOutgoingChannelRange,'primaryRateInterfaceChannelAllocationStrategy':primaryRateInterfaceChannelAllocationStrategy,'primaryRateInterfaceMaxActiveCalls':primaryRateInterfaceMaxActiveCalls,'primaryRateInterfaceSignalInformationElementEnable':primaryRateInterfaceSignalInformationElementEnable,'primaryRateInterfaceInbandToneGenerationEnable':primaryRateInterfaceInbandToneGenerationEnable,'primaryRateInterfaceInbandDtmfDialingEnable':primaryRateInterfaceInbandDtmfDialingEnable,'primaryRateInterfaceOverlapDialingEnable':primaryRateInterfaceOverlapDialingEnable,'primaryRateInterfaceCallingNameMaxLength':primaryRateInterfaceCallingNameMaxLength,'primaryRateInterfaceExclusiveBChannelSelectionEnable':primaryRateInterfaceExclusiveBChannelSelectionEnable,'primaryRateInterfaceSendingCompleteEnable':primaryRateInterfaceSendingCompleteEnable,'primaryRateInterfaceClipEnable':primaryRateInterfaceClipEnable,'primaryRateInterfaceClirEnable':primaryRateInterfaceClirEnable,'primaryRateInterfaceClirOverrideEnable':primaryRateInterfaceClirOverrideEnable,'primaryRateInterfaceSendRestartOnStartupEnable':primaryRateInterfaceSendRestartOnStartupEnable,'primaryRateInterfaceInteropGroup':primaryRateInterfaceInteropGroup,'primaryRateInterfaceInteropTable':primaryRateInterfaceInteropTable,'primaryRateInterfaceInteropEntry':primaryRateInterfaceInteropEntry,_X:primaryRateInterfaceInteropName,'primaryRateInterfaceInteropProgressIndicatorInSetupEnable':primaryRateInterfaceInteropProgressIndicatorInSetupEnable,'primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable':primaryRateInterfaceInteropProgressIndicatorInSetupAckEnable,'primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable':primaryRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable,'primaryRateInterfaceInteropProgressIndicatorInProgressEnable':primaryRateInterfaceInteropProgressIndicatorInProgressEnable,'primaryRateInterfaceInteropProgressIndicatorInAlertingEnable':primaryRateInterfaceInteropProgressIndicatorInAlertingEnable,'primaryRateInterfaceInteropProgressIndicatorInConnectEnable':primaryRateInterfaceInteropProgressIndicatorInConnectEnable,'primaryRateInterfaceInteropMaximumFacilityWaitingDelay':primaryRateInterfaceInteropMaximumFacilityWaitingDelay,'primaryRateInterfaceInteropUseImplicitInbandInfoEnable':primaryRateInterfaceInteropUseImplicitInbandInfoEnable,'basicRateInterfaceGroup':basicRateInterfaceGroup,'basicRateInterfaceTable':basicRateInterfaceTable,'basicRateInterfaceEntry':basicRateInterfaceEntry,_Y:basicRateInterfaceName,'basicRateInterfaceEndpointType':basicRateInterfaceEndpointType,'basicRateInterfaceConnectionType':basicRateInterfaceConnectionType,'basicRateInterfaceNetworkLocation':basicRateInterfaceNetworkLocation,'basicRateInterfacePreferredEncodingScheme':basicRateInterfacePreferredEncodingScheme,'basicRateInterfaceFallbackEncodingScheme':basicRateInterfaceFallbackEncodingScheme,'basicRateInterfaceChannelAllocationStrategy':basicRateInterfaceChannelAllocationStrategy,'basicRateInterfaceMaxActiveCalls':basicRateInterfaceMaxActiveCalls,'basicRateInterfaceSignalInformationElementEnable':basicRateInterfaceSignalInformationElementEnable,'basicRateInterfaceInbandToneGenerationEnable':basicRateInterfaceInbandToneGenerationEnable,'basicRateInterfaceInbandDtmfDialingEnable':basicRateInterfaceInbandDtmfDialingEnable,'basicRateInterfaceOverlapDialingEnable':basicRateInterfaceOverlapDialingEnable,'basicRateInterfaceCallingNameMaxLength':basicRateInterfaceCallingNameMaxLength,'basicRateInterfaceExclusiveBChannelSelectionEnable':basicRateInterfaceExclusiveBChannelSelectionEnable,'basicRateInterfaceSendingCompleteEnable':basicRateInterfaceSendingCompleteEnable,'basicRateInterfaceClipEnable':basicRateInterfaceClipEnable,'basicRateInterfaceClirEnable':basicRateInterfaceClirEnable,'basicRateInterfaceClirOverrideEnable':basicRateInterfaceClirOverrideEnable,'basicRateInterfaceSendRestartOnStartupEnable':basicRateInterfaceSendRestartOnStartupEnable,'basicRateInterfaceHookFlashKeypad':basicRateInterfaceHookFlashKeypad,'basicRateInterfaceKeypadReceptionTimeout':basicRateInterfaceKeypadReceptionTimeout,'basicRateInterfaceMsn':basicRateInterfaceMsn,'basicRateInterfaceMsn2':basicRateInterfaceMsn2,'basicRateInterfaceMsn3':basicRateInterfaceMsn3,'basicRateInterfaceTeiNegotiation':basicRateInterfaceTeiNegotiation,'basicRateInterfaceInteropGroup':basicRateInterfaceInteropGroup,'basicRateInterfaceInteropTable':basicRateInterfaceInteropTable,'basicRateInterfaceInteropEntry':basicRateInterfaceInteropEntry,_a:basicRateInterfaceInteropName,'basicRateInterfaceInteropProgressIndicatorInSetupEnable':basicRateInterfaceInteropProgressIndicatorInSetupEnable,'basicRateInterfaceInteropProgressIndicatorInSetupAckEnable':basicRateInterfaceInteropProgressIndicatorInSetupAckEnable,'basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable':basicRateInterfaceInteropProgressIndicatorInCallProgressForSetupEnable,'basicRateInterfaceInteropProgressIndicatorInProgressEnable':basicRateInterfaceInteropProgressIndicatorInProgressEnable,'basicRateInterfaceInteropProgressIndicatorInAlertingEnable':basicRateInterfaceInteropProgressIndicatorInAlertingEnable,'basicRateInterfaceInteropProgressIndicatorInConnectEnable':basicRateInterfaceInteropProgressIndicatorInConnectEnable,'basicRateInterfaceInteropMaximumFacilityWaitingDelay':basicRateInterfaceInteropMaximumFacilityWaitingDelay,'basicRateInterfaceInteropUseImplicitInbandInfoEnable':basicRateInterfaceInteropUseImplicitInbandInfoEnable,'basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable':basicRateInterfaceInteropAllowTeiBroadcastInPtpEnable,'bearerChannelGroup':bearerChannelGroup,'bearerChannelInfoTable':bearerChannelInfoTable,'bearerChannelInfoEntry':bearerChannelInfoEntry,_b:bearerChannelInfoIndex,'bearerChannelInfoState':bearerChannelInfoState,'signalingChannelGroup':signalingChannelGroup,'signalingChannelTable':signalingChannelTable,'signalingChannelEntry':signalingChannelEntry,_c:signalingChannelInterfaceName,'signalingChannelProtocol':signalingChannelProtocol,'signalingChannelFacilityServicesEnable':signalingChannelFacilityServicesEnable,'signalingChannelColpEnable':signalingChannelColpEnable,'signalingChannelColrEnable':signalingChannelColrEnable,'signalingChannelColrOverrideEnable':signalingChannelColrOverrideEnable,'signalingChannelConpEnable':signalingChannelConpEnable,'signalingChannelOutgoingNotifyEnable':signalingChannelOutgoingNotifyEnable,'signalingChannelAcceptedProgressCauses':signalingChannelAcceptedProgressCauses,'signalingChannelAutoCancelTimeout':signalingChannelAutoCancelTimeout,'signalingChannelDateTimeIeSupport':signalingChannelDateTimeIeSupport,'signalingChannelMaintenanceServiceCallTermination':signalingChannelMaintenanceServiceCallTermination,'signalingChannelLinkEstablishment':signalingChannelLinkEstablishment,'signalingChannelLinkEstablishmentTimer':signalingChannelLinkEstablishmentTimer,'signalingChannelAcceptedStatusCauses':signalingChannelAcceptedStatusCauses,'signalingChannelSendIsdnProgress':signalingChannelSendIsdnProgress,'signalingChannelSendProgressIndicatorIE':signalingChannelSendProgressIndicatorIE,'signalingChannelAocESupport':signalingChannelAocESupport,'signalingChannelAocDSupport':signalingChannelAocDSupport,'signalingChannelCallReroutingBehavior':signalingChannelCallReroutingBehavior,'signalingChannelDefaultCallingTon':signalingChannelDefaultCallingTon,'signalingChannelDefaultCallingNpi':signalingChannelDefaultCallingNpi,'signalingChannelDefaultCallingPi':signalingChannelDefaultCallingPi,'signalingChannelDefaultCallingSi':signalingChannelDefaultCallingSi,'signalingChannelDefaultCalledTon':signalingChannelDefaultCalledTon,'signalingChannelDefaultCalledNpi':signalingChannelDefaultCalledNpi,'signalingChannelUserSuspendedHandling':signalingChannelUserSuspendedHandling,'signalingChannelStrictHandlingErrorConditions':signalingChannelStrictHandlingErrorConditions,'signalingChannelMcidEnable':signalingChannelMcidEnable,'signalingChannelInfoTable':signalingChannelInfoTable,'signalingChannelInfoEntry':signalingChannelInfoEntry,_n:signalingChannelInfoInterfaceName,'signalingChannelInfoState':signalingChannelInfoState,'signalingChannelInteropGroup':signalingChannelInteropGroup,'signalingChannelInteropTable':signalingChannelInteropTable,'signalingChannelInteropEntry':signalingChannelInteropEntry,_o:signalingChannelInteropInterfaceName,'signalingChannelInteropCallProceedingDelay':signalingChannelInteropCallProceedingDelay,'signalingChannelInteropCallingNameDelivery':signalingChannelInteropCallingNameDelivery,'signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream':signalingChannelInteropInteropPlayLocalRingbackWhenNoMediaStream,'signalingChannelInteropInteropConsecutiveChannelIndicator':signalingChannelInteropInteropConsecutiveChannelIndicator,'signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry':signalingChannelInteropInteropAddReleaseSecondCauseOnExpiry,'physicalGroup':physicalGroup,'physicalLinkInfoTable':physicalLinkInfoTable,'physicalLinkInfoEntry':physicalLinkInfoEntry,_p:physicalLinkInfoInterfaceName,'physicalLinkInfoState':physicalLinkInfoState,'physicalLinkTable':physicalLinkTable,'physicalLinkEntry':physicalLinkEntry,_q:physicalLinkInterfaceName,'physicalLinkL1TimerT3':physicalLinkL1TimerT3,'physicalLinkClockMode':physicalLinkClockMode,'physicalLinkMonitorLinkStateEnable':physicalLinkMonitorLinkStateEnable,'autoConfigure':autoConfigure,'autoConfigureStatus':autoConfigureStatus,'lastAutoConfigureResult':lastAutoConfigureResult,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})