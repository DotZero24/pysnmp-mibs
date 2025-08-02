_Y='zxAnEthOamEventLogIndex'
_X='ZTE-AN-ETH-EFM-MIB'
_W='tenths of a second'
_V='symbols'
_U='2^32 symbols'
_T='unknown'
_S='variableSupport'
_R='eventSupport'
_Q='loopbackSupport'
_P='unidirectionalSupport'
_O='active'
_N='passive'
_M='disabled'
_L='read-create'
_K='octets'
_J='DisplayString'
_I='Bits'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-write'
_C='frames'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
class Dot3Oui(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_ZxAnEthOamObjects_ObjectIdentity=ObjectIdentity
zxAnEthOamObjects=_ZxAnEthOamObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,61))
_ZxAnEthOamTable_Object=MibTable
zxAnEthOamTable=_ZxAnEthOamTable_Object((1,3,6,1,4,1,3902,1015,61,1))
if mibBuilder.loadTexts:zxAnEthOamTable.setStatus(_A)
_ZxAnEthOamEntry_Object=MibTableRow
zxAnEthOamEntry=_ZxAnEthOamEntry_Object((1,3,6,1,4,1,3902,1015,61,1,1))
zxAnEthOamEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnEthOamEntry.setStatus(_A)
class _ZxAnEthOamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_M,2)))
_ZxAnEthOamAdminState_Type.__name__=_E
_ZxAnEthOamAdminState_Object=MibTableColumn
zxAnEthOamAdminState=_ZxAnEthOamAdminState_Object((1,3,6,1,4,1,3902,1015,61,1,1,1),_ZxAnEthOamAdminState_Type())
zxAnEthOamAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamAdminState.setStatus(_A)
class _ZxAnEthOamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_M,1),('linkFault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9),('nonOperHalfDuplex',10)))
_ZxAnEthOamOperStatus_Type.__name__=_E
_ZxAnEthOamOperStatus_Object=MibTableColumn
zxAnEthOamOperStatus=_ZxAnEthOamOperStatus_Object((1,3,6,1,4,1,3902,1015,61,1,1,2),_ZxAnEthOamOperStatus_Type())
zxAnEthOamOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamOperStatus.setStatus(_A)
class _ZxAnEthOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnEthOamMode_Type.__name__=_E
_ZxAnEthOamMode_Object=MibTableColumn
zxAnEthOamMode=_ZxAnEthOamMode_Object((1,3,6,1,4,1,3902,1015,61,1,1,3),_ZxAnEthOamMode_Type())
zxAnEthOamMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamMode.setStatus(_A)
class _ZxAnEthOamMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_ZxAnEthOamMaxOamPduSize_Type.__name__=_H
_ZxAnEthOamMaxOamPduSize_Object=MibTableColumn
zxAnEthOamMaxOamPduSize=_ZxAnEthOamMaxOamPduSize_Object((1,3,6,1,4,1,3902,1015,61,1,1,4),_ZxAnEthOamMaxOamPduSize_Type())
zxAnEthOamMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamMaxOamPduSize.setUnits(_K)
class _ZxAnEthOamConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEthOamConfigRevision_Type.__name__=_H
_ZxAnEthOamConfigRevision_Object=MibTableColumn
zxAnEthOamConfigRevision=_ZxAnEthOamConfigRevision_Object((1,3,6,1,4,1,3902,1015,61,1,1,5),_ZxAnEthOamConfigRevision_Type())
zxAnEthOamConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamConfigRevision.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamConfigRevision.setUnits(_K)
class _ZxAnEthOamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3)))
_ZxAnEthOamFunctionsSupported_Type.__name__=_I
_ZxAnEthOamFunctionsSupported_Object=MibTableColumn
zxAnEthOamFunctionsSupported=_ZxAnEthOamFunctionsSupported_Object((1,3,6,1,4,1,3902,1015,61,1,1,6),_ZxAnEthOamFunctionsSupported_Type())
zxAnEthOamFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamFunctionsSupported.setStatus(_A)
class _ZxAnEthOamHardwareInfo_Type(DisplayString):defaultValue=OctetString('Hardware Info');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnEthOamHardwareInfo_Type.__name__=_J
_ZxAnEthOamHardwareInfo_Object=MibTableColumn
zxAnEthOamHardwareInfo=_ZxAnEthOamHardwareInfo_Object((1,3,6,1,4,1,3902,1015,61,1,1,7),_ZxAnEthOamHardwareInfo_Type())
zxAnEthOamHardwareInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamHardwareInfo.setStatus(_A)
class _ZxAnEthOamSoftwareInfo_Type(DisplayString):defaultValue=OctetString('Software Info');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnEthOamSoftwareInfo_Type.__name__=_J
_ZxAnEthOamSoftwareInfo_Object=MibTableColumn
zxAnEthOamSoftwareInfo=_ZxAnEthOamSoftwareInfo_Object((1,3,6,1,4,1,3902,1015,61,1,1,8),_ZxAnEthOamSoftwareInfo_Type())
zxAnEthOamSoftwareInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamSoftwareInfo.setStatus(_A)
_ZxAnEthOamPeerTable_Object=MibTable
zxAnEthOamPeerTable=_ZxAnEthOamPeerTable_Object((1,3,6,1,4,1,3902,1015,61,2))
if mibBuilder.loadTexts:zxAnEthOamPeerTable.setStatus(_A)
_ZxAnEthOamPeerEntry_Object=MibTableRow
zxAnEthOamPeerEntry=_ZxAnEthOamPeerEntry_Object((1,3,6,1,4,1,3902,1015,61,2,1))
zxAnEthOamPeerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnEthOamPeerEntry.setStatus(_A)
_ZxAnEthOamPeerMacAddress_Type=MacAddress
_ZxAnEthOamPeerMacAddress_Object=MibTableColumn
zxAnEthOamPeerMacAddress=_ZxAnEthOamPeerMacAddress_Object((1,3,6,1,4,1,3902,1015,61,2,1,1),_ZxAnEthOamPeerMacAddress_Type())
zxAnEthOamPeerMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerMacAddress.setStatus(_A)
_ZxAnEthOamPeerVendorOui_Type=Dot3Oui
_ZxAnEthOamPeerVendorOui_Object=MibTableColumn
zxAnEthOamPeerVendorOui=_ZxAnEthOamPeerVendorOui_Object((1,3,6,1,4,1,3902,1015,61,2,1,2),_ZxAnEthOamPeerVendorOui_Type())
zxAnEthOamPeerVendorOui.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerVendorOui.setStatus(_A)
_ZxAnEthOamPeerVendorInfo_Type=Unsigned32
_ZxAnEthOamPeerVendorInfo_Object=MibTableColumn
zxAnEthOamPeerVendorInfo=_ZxAnEthOamPeerVendorInfo_Object((1,3,6,1,4,1,3902,1015,61,2,1,3),_ZxAnEthOamPeerVendorInfo_Type())
zxAnEthOamPeerVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerVendorInfo.setStatus(_A)
class _ZxAnEthOamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_T,3)))
_ZxAnEthOamPeerMode_Type.__name__=_E
_ZxAnEthOamPeerMode_Object=MibTableColumn
zxAnEthOamPeerMode=_ZxAnEthOamPeerMode_Object((1,3,6,1,4,1,3902,1015,61,2,1,4),_ZxAnEthOamPeerMode_Type())
zxAnEthOamPeerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerMode.setStatus(_A)
class _ZxAnEthOamPeerMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,1518))
_ZxAnEthOamPeerMaxOamPduSize_Type.__name__=_H
_ZxAnEthOamPeerMaxOamPduSize_Object=MibTableColumn
zxAnEthOamPeerMaxOamPduSize=_ZxAnEthOamPeerMaxOamPduSize_Object((1,3,6,1,4,1,3902,1015,61,2,1,5),_ZxAnEthOamPeerMaxOamPduSize_Type())
zxAnEthOamPeerMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamPeerMaxOamPduSize.setUnits(_K)
class _ZxAnEthOamPeerConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnEthOamPeerConfigRevision_Type.__name__=_H
_ZxAnEthOamPeerConfigRevision_Object=MibTableColumn
zxAnEthOamPeerConfigRevision=_ZxAnEthOamPeerConfigRevision_Object((1,3,6,1,4,1,3902,1015,61,2,1,6),_ZxAnEthOamPeerConfigRevision_Type())
zxAnEthOamPeerConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerConfigRevision.setStatus(_A)
class _ZxAnEthOamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3)))
_ZxAnEthOamPeerFunctionsSupported_Type.__name__=_I
_ZxAnEthOamPeerFunctionsSupported_Object=MibTableColumn
zxAnEthOamPeerFunctionsSupported=_ZxAnEthOamPeerFunctionsSupported_Object((1,3,6,1,4,1,3902,1015,61,2,1,7),_ZxAnEthOamPeerFunctionsSupported_Type())
zxAnEthOamPeerFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamPeerFunctionsSupported.setStatus(_A)
_ZxAnEthOamLoopbackTable_Object=MibTable
zxAnEthOamLoopbackTable=_ZxAnEthOamLoopbackTable_Object((1,3,6,1,4,1,3902,1015,61,3))
if mibBuilder.loadTexts:zxAnEthOamLoopbackTable.setStatus(_A)
_ZxAnEthOamLoopbackEntry_Object=MibTableRow
zxAnEthOamLoopbackEntry=_ZxAnEthOamLoopbackEntry_Object((1,3,6,1,4,1,3902,1015,61,3,1))
zxAnEthOamLoopbackEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnEthOamLoopbackEntry.setStatus(_A)
class _ZxAnEthOamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLoopback',1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_T,6)))
_ZxAnEthOamLoopbackStatus_Type.__name__=_E
_ZxAnEthOamLoopbackStatus_Object=MibTableColumn
zxAnEthOamLoopbackStatus=_ZxAnEthOamLoopbackStatus_Object((1,3,6,1,4,1,3902,1015,61,3,1,1),_ZxAnEthOamLoopbackStatus_Type())
zxAnEthOamLoopbackStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnEthOamLoopbackStatus.setStatus(_A)
class _ZxAnEthOamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_ZxAnEthOamLoopbackIgnoreRx_Type.__name__=_E
_ZxAnEthOamLoopbackIgnoreRx_Object=MibTableColumn
zxAnEthOamLoopbackIgnoreRx=_ZxAnEthOamLoopbackIgnoreRx_Object((1,3,6,1,4,1,3902,1015,61,3,1,2),_ZxAnEthOamLoopbackIgnoreRx_Type())
zxAnEthOamLoopbackIgnoreRx.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnEthOamLoopbackIgnoreRx.setStatus(_A)
class _ZxAnEthOamLoopbackResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('noResult',0),('success',1),('generalFailed',2),('noSupport',3),('unkown',4),('noSuchPort',5),('loopBackFailed',6),('portNotActive',7),('portInTesting',8),('portInService',9),('portFailures',10),('cardFailures',11),('noPvcFound',12),('unknownTestType',13)))
_ZxAnEthOamLoopbackResult_Type.__name__=_E
_ZxAnEthOamLoopbackResult_Object=MibTableColumn
zxAnEthOamLoopbackResult=_ZxAnEthOamLoopbackResult_Object((1,3,6,1,4,1,3902,1015,61,3,1,3),_ZxAnEthOamLoopbackResult_Type())
zxAnEthOamLoopbackResult.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamLoopbackResult.setStatus(_A)
_ZxAnEthOamLoopbackSend_Type=Integer32
_ZxAnEthOamLoopbackSend_Object=MibTableColumn
zxAnEthOamLoopbackSend=_ZxAnEthOamLoopbackSend_Object((1,3,6,1,4,1,3902,1015,61,3,1,4),_ZxAnEthOamLoopbackSend_Type())
zxAnEthOamLoopbackSend.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnEthOamLoopbackSend.setStatus(_A)
_ZxAnEthOamLoopbackRecv_Type=Integer32
_ZxAnEthOamLoopbackRecv_Object=MibTableColumn
zxAnEthOamLoopbackRecv=_ZxAnEthOamLoopbackRecv_Object((1,3,6,1,4,1,3902,1015,61,3,1,5),_ZxAnEthOamLoopbackRecv_Type())
zxAnEthOamLoopbackRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamLoopbackRecv.setStatus(_A)
_ZxAnEthOamStatsTable_Object=MibTable
zxAnEthOamStatsTable=_ZxAnEthOamStatsTable_Object((1,3,6,1,4,1,3902,1015,61,4))
if mibBuilder.loadTexts:zxAnEthOamStatsTable.setStatus(_A)
_ZxAnEthOamStatsEntry_Object=MibTableRow
zxAnEthOamStatsEntry=_ZxAnEthOamStatsEntry_Object((1,3,6,1,4,1,3902,1015,61,4,1))
zxAnEthOamStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnEthOamStatsEntry.setStatus(_A)
_ZxAnEthOamInformationTx_Type=Counter32
_ZxAnEthOamInformationTx_Object=MibTableColumn
zxAnEthOamInformationTx=_ZxAnEthOamInformationTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,1),_ZxAnEthOamInformationTx_Type())
zxAnEthOamInformationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamInformationTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamInformationTx.setUnits(_C)
_ZxAnEthOamInformationRx_Type=Counter32
_ZxAnEthOamInformationRx_Object=MibTableColumn
zxAnEthOamInformationRx=_ZxAnEthOamInformationRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,2),_ZxAnEthOamInformationRx_Type())
zxAnEthOamInformationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamInformationRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamInformationRx.setUnits(_C)
_ZxAnEthOamUniqueEventNotificationTx_Type=Counter32
_ZxAnEthOamUniqueEventNotificationTx_Object=MibTableColumn
zxAnEthOamUniqueEventNotificationTx=_ZxAnEthOamUniqueEventNotificationTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,3),_ZxAnEthOamUniqueEventNotificationTx_Type())
zxAnEthOamUniqueEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamUniqueEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamUniqueEventNotificationTx.setUnits(_C)
_ZxAnEthOamUniqueEventNotificationRx_Type=Counter32
_ZxAnEthOamUniqueEventNotificationRx_Object=MibTableColumn
zxAnEthOamUniqueEventNotificationRx=_ZxAnEthOamUniqueEventNotificationRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,4),_ZxAnEthOamUniqueEventNotificationRx_Type())
zxAnEthOamUniqueEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamUniqueEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamUniqueEventNotificationRx.setUnits(_C)
_ZxAnEthOamDuplicateEventNotificationTx_Type=Counter32
_ZxAnEthOamDuplicateEventNotificationTx_Object=MibTableColumn
zxAnEthOamDuplicateEventNotificationTx=_ZxAnEthOamDuplicateEventNotificationTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,5),_ZxAnEthOamDuplicateEventNotificationTx_Type())
zxAnEthOamDuplicateEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamDuplicateEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamDuplicateEventNotificationTx.setUnits(_C)
_ZxAnEthOamDuplicateEventNotificationRx_Type=Counter32
_ZxAnEthOamDuplicateEventNotificationRx_Object=MibTableColumn
zxAnEthOamDuplicateEventNotificationRx=_ZxAnEthOamDuplicateEventNotificationRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,6),_ZxAnEthOamDuplicateEventNotificationRx_Type())
zxAnEthOamDuplicateEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamDuplicateEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamDuplicateEventNotificationRx.setUnits(_C)
_ZxAnEthOamLoopbackControlTx_Type=Counter32
_ZxAnEthOamLoopbackControlTx_Object=MibTableColumn
zxAnEthOamLoopbackControlTx=_ZxAnEthOamLoopbackControlTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,7),_ZxAnEthOamLoopbackControlTx_Type())
zxAnEthOamLoopbackControlTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamLoopbackControlTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamLoopbackControlTx.setUnits(_C)
_ZxAnEthOamLoopbackControlRx_Type=Counter32
_ZxAnEthOamLoopbackControlRx_Object=MibTableColumn
zxAnEthOamLoopbackControlRx=_ZxAnEthOamLoopbackControlRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,8),_ZxAnEthOamLoopbackControlRx_Type())
zxAnEthOamLoopbackControlRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamLoopbackControlRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamLoopbackControlRx.setUnits(_C)
_ZxAnEthOamVariableRequestTx_Type=Counter32
_ZxAnEthOamVariableRequestTx_Object=MibTableColumn
zxAnEthOamVariableRequestTx=_ZxAnEthOamVariableRequestTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,9),_ZxAnEthOamVariableRequestTx_Type())
zxAnEthOamVariableRequestTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamVariableRequestTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamVariableRequestTx.setUnits(_C)
_ZxAnEthOamVariableRequestRx_Type=Counter32
_ZxAnEthOamVariableRequestRx_Object=MibTableColumn
zxAnEthOamVariableRequestRx=_ZxAnEthOamVariableRequestRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,10),_ZxAnEthOamVariableRequestRx_Type())
zxAnEthOamVariableRequestRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamVariableRequestRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamVariableRequestRx.setUnits(_C)
_ZxAnEthOamVariableResponseTx_Type=Counter32
_ZxAnEthOamVariableResponseTx_Object=MibTableColumn
zxAnEthOamVariableResponseTx=_ZxAnEthOamVariableResponseTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,11),_ZxAnEthOamVariableResponseTx_Type())
zxAnEthOamVariableResponseTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamVariableResponseTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamVariableResponseTx.setUnits(_C)
_ZxAnEthOamVariableResponseRx_Type=Counter32
_ZxAnEthOamVariableResponseRx_Object=MibTableColumn
zxAnEthOamVariableResponseRx=_ZxAnEthOamVariableResponseRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,12),_ZxAnEthOamVariableResponseRx_Type())
zxAnEthOamVariableResponseRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamVariableResponseRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamVariableResponseRx.setUnits(_C)
_ZxAnEthOamOrgSpecificTx_Type=Counter32
_ZxAnEthOamOrgSpecificTx_Object=MibTableColumn
zxAnEthOamOrgSpecificTx=_ZxAnEthOamOrgSpecificTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,13),_ZxAnEthOamOrgSpecificTx_Type())
zxAnEthOamOrgSpecificTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamOrgSpecificTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamOrgSpecificTx.setUnits(_C)
_ZxAnEthOamOrgSpecificRx_Type=Counter32
_ZxAnEthOamOrgSpecificRx_Object=MibTableColumn
zxAnEthOamOrgSpecificRx=_ZxAnEthOamOrgSpecificRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,14),_ZxAnEthOamOrgSpecificRx_Type())
zxAnEthOamOrgSpecificRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamOrgSpecificRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamOrgSpecificRx.setUnits(_C)
_ZxAnEthOamUnsupportedCodesTx_Type=Counter32
_ZxAnEthOamUnsupportedCodesTx_Object=MibTableColumn
zxAnEthOamUnsupportedCodesTx=_ZxAnEthOamUnsupportedCodesTx_Object((1,3,6,1,4,1,3902,1015,61,4,1,15),_ZxAnEthOamUnsupportedCodesTx_Type())
zxAnEthOamUnsupportedCodesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamUnsupportedCodesTx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamUnsupportedCodesTx.setUnits(_C)
_ZxAnEthOamUnsupportedCodesRx_Type=Counter32
_ZxAnEthOamUnsupportedCodesRx_Object=MibTableColumn
zxAnEthOamUnsupportedCodesRx=_ZxAnEthOamUnsupportedCodesRx_Object((1,3,6,1,4,1,3902,1015,61,4,1,16),_ZxAnEthOamUnsupportedCodesRx_Type())
zxAnEthOamUnsupportedCodesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamUnsupportedCodesRx.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamUnsupportedCodesRx.setUnits(_C)
_ZxAnEthOamFramesLostDueToOam_Type=Counter32
_ZxAnEthOamFramesLostDueToOam_Object=MibTableColumn
zxAnEthOamFramesLostDueToOam=_ZxAnEthOamFramesLostDueToOam_Object((1,3,6,1,4,1,3902,1015,61,4,1,17),_ZxAnEthOamFramesLostDueToOam_Type())
zxAnEthOamFramesLostDueToOam.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamFramesLostDueToOam.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamFramesLostDueToOam.setUnits(_C)
_ZxAnEthOamEventConfigTable_Object=MibTable
zxAnEthOamEventConfigTable=_ZxAnEthOamEventConfigTable_Object((1,3,6,1,4,1,3902,1015,61,5))
if mibBuilder.loadTexts:zxAnEthOamEventConfigTable.setStatus(_A)
_ZxAnEthOamEventConfigEntry_Object=MibTableRow
zxAnEthOamEventConfigEntry=_ZxAnEthOamEventConfigEntry_Object((1,3,6,1,4,1,3902,1015,61,5,1))
zxAnEthOamEventConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnEthOamEventConfigEntry.setStatus(_A)
_ZxAnEthOamErrSymPeriodWindowHi_Type=Unsigned32
_ZxAnEthOamErrSymPeriodWindowHi_Object=MibTableColumn
zxAnEthOamErrSymPeriodWindowHi=_ZxAnEthOamErrSymPeriodWindowHi_Object((1,3,6,1,4,1,3902,1015,61,5,1,1),_ZxAnEthOamErrSymPeriodWindowHi_Type())
zxAnEthOamErrSymPeriodWindowHi.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodWindowHi.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodWindowHi.setUnits(_U)
_ZxAnEthOamErrSymPeriodWindowLo_Type=Unsigned32
_ZxAnEthOamErrSymPeriodWindowLo_Object=MibTableColumn
zxAnEthOamErrSymPeriodWindowLo=_ZxAnEthOamErrSymPeriodWindowLo_Object((1,3,6,1,4,1,3902,1015,61,5,1,2),_ZxAnEthOamErrSymPeriodWindowLo_Type())
zxAnEthOamErrSymPeriodWindowLo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodWindowLo.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodWindowLo.setUnits(_V)
_ZxAnEthOamErrSymPeriodThresholdHi_Type=Unsigned32
_ZxAnEthOamErrSymPeriodThresholdHi_Object=MibTableColumn
zxAnEthOamErrSymPeriodThresholdHi=_ZxAnEthOamErrSymPeriodThresholdHi_Object((1,3,6,1,4,1,3902,1015,61,5,1,3),_ZxAnEthOamErrSymPeriodThresholdHi_Type())
zxAnEthOamErrSymPeriodThresholdHi.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodThresholdHi.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodThresholdHi.setUnits(_U)
_ZxAnEthOamErrSymPeriodThresholdLo_Type=Unsigned32
_ZxAnEthOamErrSymPeriodThresholdLo_Object=MibTableColumn
zxAnEthOamErrSymPeriodThresholdLo=_ZxAnEthOamErrSymPeriodThresholdLo_Object((1,3,6,1,4,1,3902,1015,61,5,1,4),_ZxAnEthOamErrSymPeriodThresholdLo_Type())
zxAnEthOamErrSymPeriodThresholdLo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodThresholdLo.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodThresholdLo.setUnits(_V)
_ZxAnEthOamErrSymPeriodEvNotifEnable_Type=TruthValue
_ZxAnEthOamErrSymPeriodEvNotifEnable_Object=MibTableColumn
zxAnEthOamErrSymPeriodEvNotifEnable=_ZxAnEthOamErrSymPeriodEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,61,5,1,5),_ZxAnEthOamErrSymPeriodEvNotifEnable_Type())
zxAnEthOamErrSymPeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrSymPeriodEvNotifEnable.setStatus(_A)
_ZxAnEthOamErrFramePeriodWindow_Type=Unsigned32
_ZxAnEthOamErrFramePeriodWindow_Object=MibTableColumn
zxAnEthOamErrFramePeriodWindow=_ZxAnEthOamErrFramePeriodWindow_Object((1,3,6,1,4,1,3902,1015,61,5,1,6),_ZxAnEthOamErrFramePeriodWindow_Type())
zxAnEthOamErrFramePeriodWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFramePeriodWindow.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrFramePeriodWindow.setUnits(_C)
_ZxAnEthOamErrFramePeriodThreshold_Type=Unsigned32
_ZxAnEthOamErrFramePeriodThreshold_Object=MibTableColumn
zxAnEthOamErrFramePeriodThreshold=_ZxAnEthOamErrFramePeriodThreshold_Object((1,3,6,1,4,1,3902,1015,61,5,1,7),_ZxAnEthOamErrFramePeriodThreshold_Type())
zxAnEthOamErrFramePeriodThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFramePeriodThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrFramePeriodThreshold.setUnits(_C)
_ZxAnEthOamErrFramePeriodEvNotifEnable_Type=TruthValue
_ZxAnEthOamErrFramePeriodEvNotifEnable_Object=MibTableColumn
zxAnEthOamErrFramePeriodEvNotifEnable=_ZxAnEthOamErrFramePeriodEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,61,5,1,8),_ZxAnEthOamErrFramePeriodEvNotifEnable_Type())
zxAnEthOamErrFramePeriodEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFramePeriodEvNotifEnable.setStatus(_A)
_ZxAnEthOamErrFrameWindow_Type=Unsigned32
_ZxAnEthOamErrFrameWindow_Object=MibTableColumn
zxAnEthOamErrFrameWindow=_ZxAnEthOamErrFrameWindow_Object((1,3,6,1,4,1,3902,1015,61,5,1,9),_ZxAnEthOamErrFrameWindow_Type())
zxAnEthOamErrFrameWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFrameWindow.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrFrameWindow.setUnits(_W)
_ZxAnEthOamErrFrameThreshold_Type=Unsigned32
_ZxAnEthOamErrFrameThreshold_Object=MibTableColumn
zxAnEthOamErrFrameThreshold=_ZxAnEthOamErrFrameThreshold_Object((1,3,6,1,4,1,3902,1015,61,5,1,10),_ZxAnEthOamErrFrameThreshold_Type())
zxAnEthOamErrFrameThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFrameThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrFrameThreshold.setUnits(_C)
_ZxAnEthOamErrFrameEvNotifEnable_Type=TruthValue
_ZxAnEthOamErrFrameEvNotifEnable_Object=MibTableColumn
zxAnEthOamErrFrameEvNotifEnable=_ZxAnEthOamErrFrameEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,61,5,1,11),_ZxAnEthOamErrFrameEvNotifEnable_Type())
zxAnEthOamErrFrameEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFrameEvNotifEnable.setStatus(_A)
class _ZxAnEthOamErrFrameSecsSummaryWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_ZxAnEthOamErrFrameSecsSummaryWindow_Type.__name__=_E
_ZxAnEthOamErrFrameSecsSummaryWindow_Object=MibTableColumn
zxAnEthOamErrFrameSecsSummaryWindow=_ZxAnEthOamErrFrameSecsSummaryWindow_Object((1,3,6,1,4,1,3902,1015,61,5,1,12),_ZxAnEthOamErrFrameSecsSummaryWindow_Type())
zxAnEthOamErrFrameSecsSummaryWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFrameSecsSummaryWindow.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrFrameSecsSummaryWindow.setUnits(_W)
class _ZxAnEthOamErrFrameSecsSummaryThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_ZxAnEthOamErrFrameSecsSummaryThreshold_Type.__name__=_E
_ZxAnEthOamErrFrameSecsSummaryThreshold_Object=MibTableColumn
zxAnEthOamErrFrameSecsSummaryThreshold=_ZxAnEthOamErrFrameSecsSummaryThreshold_Object((1,3,6,1,4,1,3902,1015,61,5,1,13),_ZxAnEthOamErrFrameSecsSummaryThreshold_Type())
zxAnEthOamErrFrameSecsSummaryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFrameSecsSummaryThreshold.setStatus(_A)
if mibBuilder.loadTexts:zxAnEthOamErrFrameSecsSummaryThreshold.setUnits('errored frame seconds')
_ZxAnEthOamErrFrameSecsEvNotifEnable_Type=TruthValue
_ZxAnEthOamErrFrameSecsEvNotifEnable_Object=MibTableColumn
zxAnEthOamErrFrameSecsEvNotifEnable=_ZxAnEthOamErrFrameSecsEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,61,5,1,14),_ZxAnEthOamErrFrameSecsEvNotifEnable_Type())
zxAnEthOamErrFrameSecsEvNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamErrFrameSecsEvNotifEnable.setStatus(_A)
_ZxAnEthOamDyingGaspEnable_Type=TruthValue
_ZxAnEthOamDyingGaspEnable_Object=MibTableColumn
zxAnEthOamDyingGaspEnable=_ZxAnEthOamDyingGaspEnable_Object((1,3,6,1,4,1,3902,1015,61,5,1,15),_ZxAnEthOamDyingGaspEnable_Type())
zxAnEthOamDyingGaspEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamDyingGaspEnable.setStatus(_A)
_ZxAnEthOamCriticalEventEnable_Type=TruthValue
_ZxAnEthOamCriticalEventEnable_Object=MibTableColumn
zxAnEthOamCriticalEventEnable=_ZxAnEthOamCriticalEventEnable_Object((1,3,6,1,4,1,3902,1015,61,5,1,16),_ZxAnEthOamCriticalEventEnable_Type())
zxAnEthOamCriticalEventEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamCriticalEventEnable.setStatus(_A)
_ZxAnEthOamEventLogTable_Object=MibTable
zxAnEthOamEventLogTable=_ZxAnEthOamEventLogTable_Object((1,3,6,1,4,1,3902,1015,61,6))
if mibBuilder.loadTexts:zxAnEthOamEventLogTable.setStatus(_A)
_ZxAnEthOamEventLogEntry_Object=MibTableRow
zxAnEthOamEventLogEntry=_ZxAnEthOamEventLogEntry_Object((1,3,6,1,4,1,3902,1015,61,6,1))
zxAnEthOamEventLogEntry.setIndexNames((0,_F,_G),(0,_X,_Y))
if mibBuilder.loadTexts:zxAnEthOamEventLogEntry.setStatus(_A)
_ZxAnEthOamEventLogIndex_Type=Unsigned32
_ZxAnEthOamEventLogIndex_Object=MibTableColumn
zxAnEthOamEventLogIndex=_ZxAnEthOamEventLogIndex_Object((1,3,6,1,4,1,3902,1015,61,6,1,1),_ZxAnEthOamEventLogIndex_Type())
zxAnEthOamEventLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnEthOamEventLogIndex.setStatus(_A)
_ZxAnEthOamEventLogTimestamp_Type=TimeStamp
_ZxAnEthOamEventLogTimestamp_Object=MibTableColumn
zxAnEthOamEventLogTimestamp=_ZxAnEthOamEventLogTimestamp_Object((1,3,6,1,4,1,3902,1015,61,6,1,2),_ZxAnEthOamEventLogTimestamp_Type())
zxAnEthOamEventLogTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogTimestamp.setStatus(_A)
_ZxAnEthOamEventLogOui_Type=Dot3Oui
_ZxAnEthOamEventLogOui_Object=MibTableColumn
zxAnEthOamEventLogOui=_ZxAnEthOamEventLogOui_Object((1,3,6,1,4,1,3902,1015,61,6,1,3),_ZxAnEthOamEventLogOui_Type())
zxAnEthOamEventLogOui.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogOui.setStatus(_A)
_ZxAnEthOamEventLogType_Type=Unsigned32
_ZxAnEthOamEventLogType_Object=MibTableColumn
zxAnEthOamEventLogType=_ZxAnEthOamEventLogType_Object((1,3,6,1,4,1,3902,1015,61,6,1,4),_ZxAnEthOamEventLogType_Type())
zxAnEthOamEventLogType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogType.setStatus(_A)
class _ZxAnEthOamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_ZxAnEthOamEventLogLocation_Type.__name__=_E
_ZxAnEthOamEventLogLocation_Object=MibTableColumn
zxAnEthOamEventLogLocation=_ZxAnEthOamEventLogLocation_Object((1,3,6,1,4,1,3902,1015,61,6,1,5),_ZxAnEthOamEventLogLocation_Type())
zxAnEthOamEventLogLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogLocation.setStatus(_A)
_ZxAnEthOamEventLogWindowHi_Type=Unsigned32
_ZxAnEthOamEventLogWindowHi_Object=MibTableColumn
zxAnEthOamEventLogWindowHi=_ZxAnEthOamEventLogWindowHi_Object((1,3,6,1,4,1,3902,1015,61,6,1,6),_ZxAnEthOamEventLogWindowHi_Type())
zxAnEthOamEventLogWindowHi.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogWindowHi.setStatus(_A)
_ZxAnEthOamEventLogWindowLo_Type=Unsigned32
_ZxAnEthOamEventLogWindowLo_Object=MibTableColumn
zxAnEthOamEventLogWindowLo=_ZxAnEthOamEventLogWindowLo_Object((1,3,6,1,4,1,3902,1015,61,6,1,7),_ZxAnEthOamEventLogWindowLo_Type())
zxAnEthOamEventLogWindowLo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogWindowLo.setStatus(_A)
_ZxAnEthOamEventLogThresholdHi_Type=Unsigned32
_ZxAnEthOamEventLogThresholdHi_Object=MibTableColumn
zxAnEthOamEventLogThresholdHi=_ZxAnEthOamEventLogThresholdHi_Object((1,3,6,1,4,1,3902,1015,61,6,1,8),_ZxAnEthOamEventLogThresholdHi_Type())
zxAnEthOamEventLogThresholdHi.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogThresholdHi.setStatus(_A)
_ZxAnEthOamEventLogThresholdLo_Type=Unsigned32
_ZxAnEthOamEventLogThresholdLo_Object=MibTableColumn
zxAnEthOamEventLogThresholdLo=_ZxAnEthOamEventLogThresholdLo_Object((1,3,6,1,4,1,3902,1015,61,6,1,9),_ZxAnEthOamEventLogThresholdLo_Type())
zxAnEthOamEventLogThresholdLo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogThresholdLo.setStatus(_A)
_ZxAnEthOamEventLogValue_Type=CounterBasedGauge64
_ZxAnEthOamEventLogValue_Object=MibTableColumn
zxAnEthOamEventLogValue=_ZxAnEthOamEventLogValue_Object((1,3,6,1,4,1,3902,1015,61,6,1,10),_ZxAnEthOamEventLogValue_Type())
zxAnEthOamEventLogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogValue.setStatus(_A)
_ZxAnEthOamEventLogRunningTotal_Type=CounterBasedGauge64
_ZxAnEthOamEventLogRunningTotal_Object=MibTableColumn
zxAnEthOamEventLogRunningTotal=_ZxAnEthOamEventLogRunningTotal_Object((1,3,6,1,4,1,3902,1015,61,6,1,11),_ZxAnEthOamEventLogRunningTotal_Type())
zxAnEthOamEventLogRunningTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogRunningTotal.setStatus(_A)
_ZxAnEthOamEventLogEventTotal_Type=Unsigned32
_ZxAnEthOamEventLogEventTotal_Object=MibTableColumn
zxAnEthOamEventLogEventTotal=_ZxAnEthOamEventLogEventTotal_Object((1,3,6,1,4,1,3902,1015,61,6,1,12),_ZxAnEthOamEventLogEventTotal_Type())
zxAnEthOamEventLogEventTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnEthOamEventLogEventTotal.setStatus(_A)
_ZxAnEthOamGlobalEnable_Type=TruthValue
_ZxAnEthOamGlobalEnable_Object=MibScalar
zxAnEthOamGlobalEnable=_ZxAnEthOamGlobalEnable_Object((1,3,6,1,4,1,3902,1015,61,7),_ZxAnEthOamGlobalEnable_Type())
zxAnEthOamGlobalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEthOamGlobalEnable.setStatus(_A)
mibBuilder.exportSymbols(_X,**{'Dot3Oui':Dot3Oui,'zxAnEthOamObjects':zxAnEthOamObjects,'zxAnEthOamTable':zxAnEthOamTable,'zxAnEthOamEntry':zxAnEthOamEntry,'zxAnEthOamAdminState':zxAnEthOamAdminState,'zxAnEthOamOperStatus':zxAnEthOamOperStatus,'zxAnEthOamMode':zxAnEthOamMode,'zxAnEthOamMaxOamPduSize':zxAnEthOamMaxOamPduSize,'zxAnEthOamConfigRevision':zxAnEthOamConfigRevision,'zxAnEthOamFunctionsSupported':zxAnEthOamFunctionsSupported,'zxAnEthOamHardwareInfo':zxAnEthOamHardwareInfo,'zxAnEthOamSoftwareInfo':zxAnEthOamSoftwareInfo,'zxAnEthOamPeerTable':zxAnEthOamPeerTable,'zxAnEthOamPeerEntry':zxAnEthOamPeerEntry,'zxAnEthOamPeerMacAddress':zxAnEthOamPeerMacAddress,'zxAnEthOamPeerVendorOui':zxAnEthOamPeerVendorOui,'zxAnEthOamPeerVendorInfo':zxAnEthOamPeerVendorInfo,'zxAnEthOamPeerMode':zxAnEthOamPeerMode,'zxAnEthOamPeerMaxOamPduSize':zxAnEthOamPeerMaxOamPduSize,'zxAnEthOamPeerConfigRevision':zxAnEthOamPeerConfigRevision,'zxAnEthOamPeerFunctionsSupported':zxAnEthOamPeerFunctionsSupported,'zxAnEthOamLoopbackTable':zxAnEthOamLoopbackTable,'zxAnEthOamLoopbackEntry':zxAnEthOamLoopbackEntry,'zxAnEthOamLoopbackStatus':zxAnEthOamLoopbackStatus,'zxAnEthOamLoopbackIgnoreRx':zxAnEthOamLoopbackIgnoreRx,'zxAnEthOamLoopbackResult':zxAnEthOamLoopbackResult,'zxAnEthOamLoopbackSend':zxAnEthOamLoopbackSend,'zxAnEthOamLoopbackRecv':zxAnEthOamLoopbackRecv,'zxAnEthOamStatsTable':zxAnEthOamStatsTable,'zxAnEthOamStatsEntry':zxAnEthOamStatsEntry,'zxAnEthOamInformationTx':zxAnEthOamInformationTx,'zxAnEthOamInformationRx':zxAnEthOamInformationRx,'zxAnEthOamUniqueEventNotificationTx':zxAnEthOamUniqueEventNotificationTx,'zxAnEthOamUniqueEventNotificationRx':zxAnEthOamUniqueEventNotificationRx,'zxAnEthOamDuplicateEventNotificationTx':zxAnEthOamDuplicateEventNotificationTx,'zxAnEthOamDuplicateEventNotificationRx':zxAnEthOamDuplicateEventNotificationRx,'zxAnEthOamLoopbackControlTx':zxAnEthOamLoopbackControlTx,'zxAnEthOamLoopbackControlRx':zxAnEthOamLoopbackControlRx,'zxAnEthOamVariableRequestTx':zxAnEthOamVariableRequestTx,'zxAnEthOamVariableRequestRx':zxAnEthOamVariableRequestRx,'zxAnEthOamVariableResponseTx':zxAnEthOamVariableResponseTx,'zxAnEthOamVariableResponseRx':zxAnEthOamVariableResponseRx,'zxAnEthOamOrgSpecificTx':zxAnEthOamOrgSpecificTx,'zxAnEthOamOrgSpecificRx':zxAnEthOamOrgSpecificRx,'zxAnEthOamUnsupportedCodesTx':zxAnEthOamUnsupportedCodesTx,'zxAnEthOamUnsupportedCodesRx':zxAnEthOamUnsupportedCodesRx,'zxAnEthOamFramesLostDueToOam':zxAnEthOamFramesLostDueToOam,'zxAnEthOamEventConfigTable':zxAnEthOamEventConfigTable,'zxAnEthOamEventConfigEntry':zxAnEthOamEventConfigEntry,'zxAnEthOamErrSymPeriodWindowHi':zxAnEthOamErrSymPeriodWindowHi,'zxAnEthOamErrSymPeriodWindowLo':zxAnEthOamErrSymPeriodWindowLo,'zxAnEthOamErrSymPeriodThresholdHi':zxAnEthOamErrSymPeriodThresholdHi,'zxAnEthOamErrSymPeriodThresholdLo':zxAnEthOamErrSymPeriodThresholdLo,'zxAnEthOamErrSymPeriodEvNotifEnable':zxAnEthOamErrSymPeriodEvNotifEnable,'zxAnEthOamErrFramePeriodWindow':zxAnEthOamErrFramePeriodWindow,'zxAnEthOamErrFramePeriodThreshold':zxAnEthOamErrFramePeriodThreshold,'zxAnEthOamErrFramePeriodEvNotifEnable':zxAnEthOamErrFramePeriodEvNotifEnable,'zxAnEthOamErrFrameWindow':zxAnEthOamErrFrameWindow,'zxAnEthOamErrFrameThreshold':zxAnEthOamErrFrameThreshold,'zxAnEthOamErrFrameEvNotifEnable':zxAnEthOamErrFrameEvNotifEnable,'zxAnEthOamErrFrameSecsSummaryWindow':zxAnEthOamErrFrameSecsSummaryWindow,'zxAnEthOamErrFrameSecsSummaryThreshold':zxAnEthOamErrFrameSecsSummaryThreshold,'zxAnEthOamErrFrameSecsEvNotifEnable':zxAnEthOamErrFrameSecsEvNotifEnable,'zxAnEthOamDyingGaspEnable':zxAnEthOamDyingGaspEnable,'zxAnEthOamCriticalEventEnable':zxAnEthOamCriticalEventEnable,'zxAnEthOamEventLogTable':zxAnEthOamEventLogTable,'zxAnEthOamEventLogEntry':zxAnEthOamEventLogEntry,_Y:zxAnEthOamEventLogIndex,'zxAnEthOamEventLogTimestamp':zxAnEthOamEventLogTimestamp,'zxAnEthOamEventLogOui':zxAnEthOamEventLogOui,'zxAnEthOamEventLogType':zxAnEthOamEventLogType,'zxAnEthOamEventLogLocation':zxAnEthOamEventLogLocation,'zxAnEthOamEventLogWindowHi':zxAnEthOamEventLogWindowHi,'zxAnEthOamEventLogWindowLo':zxAnEthOamEventLogWindowLo,'zxAnEthOamEventLogThresholdHi':zxAnEthOamEventLogThresholdHi,'zxAnEthOamEventLogThresholdLo':zxAnEthOamEventLogThresholdLo,'zxAnEthOamEventLogValue':zxAnEthOamEventLogValue,'zxAnEthOamEventLogRunningTotal':zxAnEthOamEventLogRunningTotal,'zxAnEthOamEventLogEventTotal':zxAnEthOamEventLogEventTotal,'zxAnEthOamGlobalEnable':zxAnEthOamGlobalEnable})