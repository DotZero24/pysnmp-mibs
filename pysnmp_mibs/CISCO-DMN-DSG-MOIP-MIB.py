_O='active'
_N='suspended'
_M='stopped'
_L='notInit'
_K='moipIPOStreamStatusID'
_J='moipIPOConfigID'
_I='none'
_H='CISCO-DMN-DSG-MOIP-MIB'
_G='yes'
_F='no'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoDSGMOIP=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,35))
if mibBuilder.loadTexts:ciscoDSGMOIP.setRevisions(('2012-03-20 11:00','2010-08-24 07:30'))
_MoipIPOTable_ObjectIdentity=ObjectIdentity
moipIPOTable=_MoipIPOTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,35,1))
_MoipIPOConfigTable_Object=MibTable
moipIPOConfigTable=_MoipIPOConfigTable_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1))
if mibBuilder.loadTexts:moipIPOConfigTable.setStatus(_A)
_MoipIPOConfigEntry_Object=MibTableRow
moipIPOConfigEntry=_MoipIPOConfigEntry_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1))
moipIPOConfigEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:moipIPOConfigEntry.setStatus(_A)
class _MoipIPOConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_MoipIPOConfigID_Type.__name__=_B
_MoipIPOConfigID_Object=MibTableColumn
moipIPOConfigID=_MoipIPOConfigID_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,1),_MoipIPOConfigID_Type())
moipIPOConfigID.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOConfigID.setStatus(_A)
class _MoipIPOConfigOutputEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_F,1),(_G,3)))
_MoipIPOConfigOutputEnabled_Type.__name__=_B
_MoipIPOConfigOutputEnabled_Object=MibTableColumn
moipIPOConfigOutputEnabled=_MoipIPOConfigOutputEnabled_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,2),_MoipIPOConfigOutputEnabled_Type())
moipIPOConfigOutputEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigOutputEnabled.setStatus(_A)
class _MoipIPOConfigInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MoipIPOConfigInstanceName_Type.__name__=_E
_MoipIPOConfigInstanceName_Object=MibTableColumn
moipIPOConfigInstanceName=_MoipIPOConfigInstanceName_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,3),_MoipIPOConfigInstanceName_Type())
moipIPOConfigInstanceName.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigInstanceName.setStatus(_A)
class _MoipIPOConfigTPProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('rtp',2)))
_MoipIPOConfigTPProtocol_Type.__name__=_B
_MoipIPOConfigTPProtocol_Object=MibTableColumn
moipIPOConfigTPProtocol=_MoipIPOConfigTPProtocol_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,4),_MoipIPOConfigTPProtocol_Type())
moipIPOConfigTPProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigTPProtocol.setStatus(_A)
class _MoipIPOConfigIPVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MoipIPOConfigIPVer_Type.__name__=_E
_MoipIPOConfigIPVer_Object=MibTableColumn
moipIPOConfigIPVer=_MoipIPOConfigIPVer_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,5),_MoipIPOConfigIPVer_Type())
moipIPOConfigIPVer.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOConfigIPVer.setStatus(_A)
_MoipIPOConfigDestIPAddr_Type=IpAddress
_MoipIPOConfigDestIPAddr_Object=MibTableColumn
moipIPOConfigDestIPAddr=_MoipIPOConfigDestIPAddr_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,6),_MoipIPOConfigDestIPAddr_Type())
moipIPOConfigDestIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigDestIPAddr.setStatus(_A)
_MoipIPOConfigSAPMulticastIPAddr_Type=IpAddress
_MoipIPOConfigSAPMulticastIPAddr_Object=MibTableColumn
moipIPOConfigSAPMulticastIPAddr=_MoipIPOConfigSAPMulticastIPAddr_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,7),_MoipIPOConfigSAPMulticastIPAddr_Type())
moipIPOConfigSAPMulticastIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigSAPMulticastIPAddr.setStatus(_A)
class _MoipIPOConfigDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_MoipIPOConfigDestPort_Type.__name__=_B
_MoipIPOConfigDestPort_Object=MibTableColumn
moipIPOConfigDestPort=_MoipIPOConfigDestPort_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,8),_MoipIPOConfigDestPort_Type())
moipIPOConfigDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigDestPort.setStatus(_A)
class _MoipIPOConfigSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MoipIPOConfigSrcPort_Type.__name__=_B
_MoipIPOConfigSrcPort_Object=MibTableColumn
moipIPOConfigSrcPort=_MoipIPOConfigSrcPort_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,9),_MoipIPOConfigSrcPort_Type())
moipIPOConfigSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigSrcPort.setStatus(_A)
class _MoipIPOConfigMinIPPerSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MoipIPOConfigMinIPPerSec_Type.__name__=_B
_MoipIPOConfigMinIPPerSec_Object=MibTableColumn
moipIPOConfigMinIPPerSec=_MoipIPOConfigMinIPPerSec_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,10),_MoipIPOConfigMinIPPerSec_Type())
moipIPOConfigMinIPPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigMinIPPerSec.setStatus(_A)
class _MoipIPOConfigPCRAddition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MoipIPOConfigPCRAddition_Type.__name__=_B
_MoipIPOConfigPCRAddition_Object=MibTableColumn
moipIPOConfigPCRAddition=_MoipIPOConfigPCRAddition_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,11),_MoipIPOConfigPCRAddition_Type())
moipIPOConfigPCRAddition.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigPCRAddition.setStatus(_A)
class _MoipIPOConfigPCRStartNewPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MoipIPOConfigPCRStartNewPkt_Type.__name__=_B
_MoipIPOConfigPCRStartNewPkt_Object=MibTableColumn
moipIPOConfigPCRStartNewPkt=_MoipIPOConfigPCRStartNewPkt_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,12),_MoipIPOConfigPCRStartNewPkt_Type())
moipIPOConfigPCRStartNewPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigPCRStartNewPkt.setStatus(_A)
class _MoipIPOConfigSendSAP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('rfc2327',2)))
_MoipIPOConfigSendSAP_Type.__name__=_B
_MoipIPOConfigSendSAP_Object=MibTableColumn
moipIPOConfigSendSAP=_MoipIPOConfigSendSAP_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,13),_MoipIPOConfigSendSAP_Type())
moipIPOConfigSendSAP.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigSendSAP.setStatus(_A)
class _MoipIPOConfigUseSAPStr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('userString',1),('sdtChName',2)))
_MoipIPOConfigUseSAPStr_Type.__name__=_B
_MoipIPOConfigUseSAPStr_Object=MibTableColumn
moipIPOConfigUseSAPStr=_MoipIPOConfigUseSAPStr_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,14),_MoipIPOConfigUseSAPStr_Type())
moipIPOConfigUseSAPStr.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigUseSAPStr.setStatus(_A)
class _MoipIPOConfigMaxTransPktPerIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_MoipIPOConfigMaxTransPktPerIP_Type.__name__=_B
_MoipIPOConfigMaxTransPktPerIP_Object=MibTableColumn
moipIPOConfigMaxTransPktPerIP=_MoipIPOConfigMaxTransPktPerIP_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,15),_MoipIPOConfigMaxTransPktPerIP_Type())
moipIPOConfigMaxTransPktPerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigMaxTransPktPerIP.setStatus(_A)
class _MoipIPOConfigSAPStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MoipIPOConfigSAPStr_Type.__name__=_E
_MoipIPOConfigSAPStr_Object=MibTableColumn
moipIPOConfigSAPStr=_MoipIPOConfigSAPStr_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,16),_MoipIPOConfigSAPStr_Type())
moipIPOConfigSAPStr.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigSAPStr.setStatus(_A)
class _MoipIPOConfigInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('data1',2),('data2',3),('both',4),('redundancy',5)))
_MoipIPOConfigInterfaceMode_Type.__name__=_B
_MoipIPOConfigInterfaceMode_Object=MibTableColumn
moipIPOConfigInterfaceMode=_MoipIPOConfigInterfaceMode_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,17),_MoipIPOConfigInterfaceMode_Type())
moipIPOConfigInterfaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigInterfaceMode.setStatus(_A)
class _MoipIPOConfigBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,206000000))
_MoipIPOConfigBitRate_Type.__name__=_B
_MoipIPOConfigBitRate_Object=MibTableColumn
moipIPOConfigBitRate=_MoipIPOConfigBitRate_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,18),_MoipIPOConfigBitRate_Type())
moipIPOConfigBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigBitRate.setStatus(_A)
class _MoipIPOConfigTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MoipIPOConfigTOS_Type.__name__=_B
_MoipIPOConfigTOS_Object=MibTableColumn
moipIPOConfigTOS=_MoipIPOConfigTOS_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,19),_MoipIPOConfigTOS_Type())
moipIPOConfigTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigTOS.setStatus(_A)
class _MoipIPOConfigTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MoipIPOConfigTTL_Type.__name__=_B
_MoipIPOConfigTTL_Object=MibTableColumn
moipIPOConfigTTL=_MoipIPOConfigTTL_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,20),_MoipIPOConfigTTL_Type())
moipIPOConfigTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigTTL.setStatus(_A)
class _MoipIPOConfigSAPDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_MoipIPOConfigSAPDestPort_Type.__name__=_B
_MoipIPOConfigSAPDestPort_Object=MibTableColumn
moipIPOConfigSAPDestPort=_MoipIPOConfigSAPDestPort_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,21),_MoipIPOConfigSAPDestPort_Type())
moipIPOConfigSAPDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOConfigSAPDestPort.setStatus(_A)
class _MoipIPOFECMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('oneD',2),('twoD',3)))
_MoipIPOFECMode_Type.__name__=_B
_MoipIPOFECMode_Object=MibTableColumn
moipIPOFECMode=_MoipIPOFECMode_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,22),_MoipIPOFECMode_Type())
moipIPOFECMode.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOFECMode.setStatus(_A)
class _MoipIPOFECColDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_MoipIPOFECColDepth_Type.__name__=_B
_MoipIPOFECColDepth_Object=MibTableColumn
moipIPOFECColDepth=_MoipIPOFECColDepth_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,23),_MoipIPOFECColDepth_Type())
moipIPOFECColDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOFECColDepth.setStatus(_A)
class _MoipIPOFECRowWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_MoipIPOFECRowWidth_Type.__name__=_B
_MoipIPOFECRowWidth_Object=MibTableColumn
moipIPOFECRowWidth=_MoipIPOFECRowWidth_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,24),_MoipIPOFECRowWidth_Type())
moipIPOFECRowWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOFECRowWidth.setStatus(_A)
class _MoipIPOAnnexType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('annexA',1),('annexB',2)))
_MoipIPOAnnexType_Type.__name__=_B
_MoipIPOAnnexType_Object=MibTableColumn
moipIPOAnnexType=_MoipIPOAnnexType_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,25),_MoipIPOAnnexType_Type())
moipIPOAnnexType.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOAnnexType.setStatus(_A)
class _MoipIPOFEC1UDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65534))
_MoipIPOFEC1UDPPort_Type.__name__=_B
_MoipIPOFEC1UDPPort_Object=MibTableColumn
moipIPOFEC1UDPPort=_MoipIPOFEC1UDPPort_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,26),_MoipIPOFEC1UDPPort_Type())
moipIPOFEC1UDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOFEC1UDPPort.setStatus(_A)
class _MoipIPOFEC2UDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65534))
_MoipIPOFEC2UDPPort_Type.__name__=_B
_MoipIPOFEC2UDPPort_Object=MibTableColumn
moipIPOFEC2UDPPort=_MoipIPOFEC2UDPPort_Object((1,3,6,1,4,1,1429,2,2,5,35,1,1,1,27),_MoipIPOFEC2UDPPort_Type())
moipIPOFEC2UDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:moipIPOFEC2UDPPort.setStatus(_A)
_MoipIPOStreamStatusTable_Object=MibTable
moipIPOStreamStatusTable=_MoipIPOStreamStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2))
if mibBuilder.loadTexts:moipIPOStreamStatusTable.setStatus(_A)
_MoipIPOStreamStatusEntry_Object=MibTableRow
moipIPOStreamStatusEntry=_MoipIPOStreamStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2,1))
moipIPOStreamStatusEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:moipIPOStreamStatusEntry.setStatus(_A)
class _MoipIPOStreamStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_MoipIPOStreamStatusID_Type.__name__=_B
_MoipIPOStreamStatusID_Object=MibTableColumn
moipIPOStreamStatusID=_MoipIPOStreamStatusID_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2,1,1),_MoipIPOStreamStatusID_Type())
moipIPOStreamStatusID.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStreamStatusID.setStatus(_A)
class _MoipIPOStreamStatusIntf1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),('muted',4),(_O,5)))
_MoipIPOStreamStatusIntf1_Type.__name__=_B
_MoipIPOStreamStatusIntf1_Object=MibTableColumn
moipIPOStreamStatusIntf1=_MoipIPOStreamStatusIntf1_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2,1,2),_MoipIPOStreamStatusIntf1_Type())
moipIPOStreamStatusIntf1.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStreamStatusIntf1.setStatus(_A)
class _MoipIPOStreamStatusIntf2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),('muted',4),(_O,5)))
_MoipIPOStreamStatusIntf2_Type.__name__=_B
_MoipIPOStreamStatusIntf2_Object=MibTableColumn
moipIPOStreamStatusIntf2=_MoipIPOStreamStatusIntf2_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2,1,3),_MoipIPOStreamStatusIntf2_Type())
moipIPOStreamStatusIntf2.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStreamStatusIntf2.setStatus(_A)
class _MoipIPOStreamStatusContentOvfl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MoipIPOStreamStatusContentOvfl_Type.__name__=_B
_MoipIPOStreamStatusContentOvfl_Object=MibTableColumn
moipIPOStreamStatusContentOvfl=_MoipIPOStreamStatusContentOvfl_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2,1,4),_MoipIPOStreamStatusContentOvfl_Type())
moipIPOStreamStatusContentOvfl.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStreamStatusContentOvfl.setStatus(_A)
class _MoipIPOStreamStatusLinkOvfl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MoipIPOStreamStatusLinkOvfl_Type.__name__=_B
_MoipIPOStreamStatusLinkOvfl_Object=MibTableColumn
moipIPOStreamStatusLinkOvfl=_MoipIPOStreamStatusLinkOvfl_Object((1,3,6,1,4,1,1429,2,2,5,35,1,2,1,5),_MoipIPOStreamStatusLinkOvfl_Type())
moipIPOStreamStatusLinkOvfl.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStreamStatusLinkOvfl.setStatus(_A)
_MoipIPOInfo_ObjectIdentity=ObjectIdentity
moipIPOInfo=_MoipIPOInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,35,2))
class _MoipIPOStatsHWGlobalError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MoipIPOStatsHWGlobalError_Type.__name__=_B
_MoipIPOStatsHWGlobalError_Object=MibScalar
moipIPOStatsHWGlobalError=_MoipIPOStatsHWGlobalError_Object((1,3,6,1,4,1,1429,2,2,5,35,2,1),_MoipIPOStatsHWGlobalError_Type())
moipIPOStatsHWGlobalError.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStatsHWGlobalError.setStatus(_A)
class _MoipIPOStatsStreamError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_MoipIPOStatsStreamError_Type.__name__=_B
_MoipIPOStatsStreamError_Object=MibScalar
moipIPOStatsStreamError=_MoipIPOStatsStreamError_Object((1,3,6,1,4,1,1429,2,2,5,35,2,2),_MoipIPOStatsStreamError_Type())
moipIPOStatsStreamError.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStatsStreamError.setStatus(_A)
class _MoipIPOStatsBandwidthConf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_MoipIPOStatsBandwidthConf_Type.__name__=_E
_MoipIPOStatsBandwidthConf_Object=MibScalar
moipIPOStatsBandwidthConf=_MoipIPOStatsBandwidthConf_Object((1,3,6,1,4,1,1429,2,2,5,35,2,3),_MoipIPOStatsBandwidthConf_Type())
moipIPOStatsBandwidthConf.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStatsBandwidthConf.setStatus(_A)
class _MoipIPOStatsBandwidthActIntf1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_MoipIPOStatsBandwidthActIntf1_Type.__name__=_E
_MoipIPOStatsBandwidthActIntf1_Object=MibScalar
moipIPOStatsBandwidthActIntf1=_MoipIPOStatsBandwidthActIntf1_Object((1,3,6,1,4,1,1429,2,2,5,35,2,4),_MoipIPOStatsBandwidthActIntf1_Type())
moipIPOStatsBandwidthActIntf1.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStatsBandwidthActIntf1.setStatus(_A)
class _MoipIPOStatsBandwidthActIntf2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_MoipIPOStatsBandwidthActIntf2_Type.__name__=_E
_MoipIPOStatsBandwidthActIntf2_Object=MibScalar
moipIPOStatsBandwidthActIntf2=_MoipIPOStatsBandwidthActIntf2_Object((1,3,6,1,4,1,1429,2,2,5,35,2,5),_MoipIPOStatsBandwidthActIntf2_Type())
moipIPOStatsBandwidthActIntf2.setMaxAccess(_D)
if mibBuilder.loadTexts:moipIPOStatsBandwidthActIntf2.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'ciscoDSGMOIP':ciscoDSGMOIP,'moipIPOTable':moipIPOTable,'moipIPOConfigTable':moipIPOConfigTable,'moipIPOConfigEntry':moipIPOConfigEntry,_J:moipIPOConfigID,'moipIPOConfigOutputEnabled':moipIPOConfigOutputEnabled,'moipIPOConfigInstanceName':moipIPOConfigInstanceName,'moipIPOConfigTPProtocol':moipIPOConfigTPProtocol,'moipIPOConfigIPVer':moipIPOConfigIPVer,'moipIPOConfigDestIPAddr':moipIPOConfigDestIPAddr,'moipIPOConfigSAPMulticastIPAddr':moipIPOConfigSAPMulticastIPAddr,'moipIPOConfigDestPort':moipIPOConfigDestPort,'moipIPOConfigSrcPort':moipIPOConfigSrcPort,'moipIPOConfigMinIPPerSec':moipIPOConfigMinIPPerSec,'moipIPOConfigPCRAddition':moipIPOConfigPCRAddition,'moipIPOConfigPCRStartNewPkt':moipIPOConfigPCRStartNewPkt,'moipIPOConfigSendSAP':moipIPOConfigSendSAP,'moipIPOConfigUseSAPStr':moipIPOConfigUseSAPStr,'moipIPOConfigMaxTransPktPerIP':moipIPOConfigMaxTransPktPerIP,'moipIPOConfigSAPStr':moipIPOConfigSAPStr,'moipIPOConfigInterfaceMode':moipIPOConfigInterfaceMode,'moipIPOConfigBitRate':moipIPOConfigBitRate,'moipIPOConfigTOS':moipIPOConfigTOS,'moipIPOConfigTTL':moipIPOConfigTTL,'moipIPOConfigSAPDestPort':moipIPOConfigSAPDestPort,'moipIPOFECMode':moipIPOFECMode,'moipIPOFECColDepth':moipIPOFECColDepth,'moipIPOFECRowWidth':moipIPOFECRowWidth,'moipIPOAnnexType':moipIPOAnnexType,'moipIPOFEC1UDPPort':moipIPOFEC1UDPPort,'moipIPOFEC2UDPPort':moipIPOFEC2UDPPort,'moipIPOStreamStatusTable':moipIPOStreamStatusTable,'moipIPOStreamStatusEntry':moipIPOStreamStatusEntry,_K:moipIPOStreamStatusID,'moipIPOStreamStatusIntf1':moipIPOStreamStatusIntf1,'moipIPOStreamStatusIntf2':moipIPOStreamStatusIntf2,'moipIPOStreamStatusContentOvfl':moipIPOStreamStatusContentOvfl,'moipIPOStreamStatusLinkOvfl':moipIPOStreamStatusLinkOvfl,'moipIPOInfo':moipIPOInfo,'moipIPOStatsHWGlobalError':moipIPOStatsHWGlobalError,'moipIPOStatsStreamError':moipIPOStatsStreamError,'moipIPOStatsBandwidthConf':moipIPOStatsBandwidthConf,'moipIPOStatsBandwidthActIntf1':moipIPOStatsBandwidthActIntf1,'moipIPOStatsBandwidthActIntf2':moipIPOStatsBandwidthActIntf2})