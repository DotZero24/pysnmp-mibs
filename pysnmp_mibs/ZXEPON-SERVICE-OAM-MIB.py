_W='dot3OamEventLogIndex'
_V='ZXEPON-SERVICE-OAM-MIB'
_U='tenths of a second'
_T='symbols'
_S='2^32 symbols'
_R='unknown'
_Q='variableSupport'
_P='eventSupport'
_O='loopbackSupport'
_N='unidirectionalSupport'
_M='active'
_L='passive'
_K='disabled'
_J='octets'
_I='Bits'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='frames'
_C='read-write'
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
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
zxAnEponMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnEponMib')
class Dot3Oui(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_Dot3OamObjects_ObjectIdentity=ObjectIdentity
dot3OamObjects=_Dot3OamObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1010,1,6))
_Dot3OamTable_Object=MibTable
dot3OamTable=_Dot3OamTable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1))
if mibBuilder.loadTexts:dot3OamTable.setStatus(_A)
_Dot3OamEntry_Object=MibTableRow
dot3OamEntry=_Dot3OamEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1))
dot3OamEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamEntry.setStatus(_A)
class _Dot3OamAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_K,2)))
_Dot3OamAdminState_Type.__name__=_E
_Dot3OamAdminState_Object=MibTableColumn
dot3OamAdminState=_Dot3OamAdminState_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1,1),_Dot3OamAdminState_Type())
dot3OamAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamAdminState.setStatus(_A)
class _Dot3OamOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_K,1),('linkFault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9),('nonOperHalfDuplex',10)))
_Dot3OamOperStatus_Type.__name__=_E
_Dot3OamOperStatus_Object=MibTableColumn
dot3OamOperStatus=_Dot3OamOperStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1,2),_Dot3OamOperStatus_Type())
dot3OamOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamOperStatus.setStatus(_A)
class _Dot3OamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_Dot3OamMode_Type.__name__=_E
_Dot3OamMode_Object=MibTableColumn
dot3OamMode=_Dot3OamMode_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1,3),_Dot3OamMode_Type())
dot3OamMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamMode.setStatus(_A)
class _Dot3OamMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_Dot3OamMaxOamPduSize_Type.__name__=_H
_Dot3OamMaxOamPduSize_Object=MibTableColumn
dot3OamMaxOamPduSize=_Dot3OamMaxOamPduSize_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1,4),_Dot3OamMaxOamPduSize_Type())
dot3OamMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:dot3OamMaxOamPduSize.setUnits(_J)
class _Dot3OamConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3OamConfigRevision_Type.__name__=_H
_Dot3OamConfigRevision_Object=MibTableColumn
dot3OamConfigRevision=_Dot3OamConfigRevision_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1,5),_Dot3OamConfigRevision_Type())
dot3OamConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamConfigRevision.setStatus(_A)
if mibBuilder.loadTexts:dot3OamConfigRevision.setUnits(_J)
class _Dot3OamFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_Dot3OamFunctionsSupported_Type.__name__=_I
_Dot3OamFunctionsSupported_Object=MibTableColumn
dot3OamFunctionsSupported=_Dot3OamFunctionsSupported_Object((1,3,6,1,4,1,3902,1015,1010,1,6,1,1,6),_Dot3OamFunctionsSupported_Type())
dot3OamFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamFunctionsSupported.setStatus(_A)
_Dot3OamPeerTable_Object=MibTable
dot3OamPeerTable=_Dot3OamPeerTable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2))
if mibBuilder.loadTexts:dot3OamPeerTable.setStatus(_A)
_Dot3OamPeerEntry_Object=MibTableRow
dot3OamPeerEntry=_Dot3OamPeerEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1))
dot3OamPeerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamPeerEntry.setStatus(_A)
_Dot3OamPeerMacAddress_Type=MacAddress
_Dot3OamPeerMacAddress_Object=MibTableColumn
dot3OamPeerMacAddress=_Dot3OamPeerMacAddress_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,1),_Dot3OamPeerMacAddress_Type())
dot3OamPeerMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerMacAddress.setStatus(_A)
_Dot3OamPeerVendorOui_Type=Dot3Oui
_Dot3OamPeerVendorOui_Object=MibTableColumn
dot3OamPeerVendorOui=_Dot3OamPeerVendorOui_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,2),_Dot3OamPeerVendorOui_Type())
dot3OamPeerVendorOui.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerVendorOui.setStatus(_A)
_Dot3OamPeerVendorInfo_Type=Unsigned32
_Dot3OamPeerVendorInfo_Object=MibTableColumn
dot3OamPeerVendorInfo=_Dot3OamPeerVendorInfo_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,3),_Dot3OamPeerVendorInfo_Type())
dot3OamPeerVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerVendorInfo.setStatus(_A)
class _Dot3OamPeerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_R,3)))
_Dot3OamPeerMode_Type.__name__=_E
_Dot3OamPeerMode_Object=MibTableColumn
dot3OamPeerMode=_Dot3OamPeerMode_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,4),_Dot3OamPeerMode_Type())
dot3OamPeerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerMode.setStatus(_A)
class _Dot3OamPeerMaxOamPduSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,1518))
_Dot3OamPeerMaxOamPduSize_Type.__name__=_H
_Dot3OamPeerMaxOamPduSize_Object=MibTableColumn
dot3OamPeerMaxOamPduSize=_Dot3OamPeerMaxOamPduSize_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,5),_Dot3OamPeerMaxOamPduSize_Type())
dot3OamPeerMaxOamPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerMaxOamPduSize.setStatus(_A)
if mibBuilder.loadTexts:dot3OamPeerMaxOamPduSize.setUnits(_J)
class _Dot3OamPeerConfigRevision_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3OamPeerConfigRevision_Type.__name__=_H
_Dot3OamPeerConfigRevision_Object=MibTableColumn
dot3OamPeerConfigRevision=_Dot3OamPeerConfigRevision_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,6),_Dot3OamPeerConfigRevision_Type())
dot3OamPeerConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerConfigRevision.setStatus(_A)
class _Dot3OamPeerFunctionsSupported_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_Dot3OamPeerFunctionsSupported_Type.__name__=_I
_Dot3OamPeerFunctionsSupported_Object=MibTableColumn
dot3OamPeerFunctionsSupported=_Dot3OamPeerFunctionsSupported_Object((1,3,6,1,4,1,3902,1015,1010,1,6,2,1,7),_Dot3OamPeerFunctionsSupported_Type())
dot3OamPeerFunctionsSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerFunctionsSupported.setStatus(_A)
_Dot3OamLoopbackTable_Object=MibTable
dot3OamLoopbackTable=_Dot3OamLoopbackTable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,3))
if mibBuilder.loadTexts:dot3OamLoopbackTable.setStatus(_A)
_Dot3OamLoopbackEntry_Object=MibTableRow
dot3OamLoopbackEntry=_Dot3OamLoopbackEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,6,3,1))
dot3OamLoopbackEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamLoopbackEntry.setStatus(_A)
class _Dot3OamLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLoopback',1),('initiatingLoopback',2),('remoteLoopback',3),('terminatingLoopback',4),('localLoopback',5),(_R,6)))
_Dot3OamLoopbackStatus_Type.__name__=_E
_Dot3OamLoopbackStatus_Object=MibTableColumn
dot3OamLoopbackStatus=_Dot3OamLoopbackStatus_Object((1,3,6,1,4,1,3902,1015,1010,1,6,3,1,1),_Dot3OamLoopbackStatus_Type())
dot3OamLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamLoopbackStatus.setStatus(_A)
class _Dot3OamLoopbackIgnoreRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('process',2)))
_Dot3OamLoopbackIgnoreRx_Type.__name__=_E
_Dot3OamLoopbackIgnoreRx_Object=MibTableColumn
dot3OamLoopbackIgnoreRx=_Dot3OamLoopbackIgnoreRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,3,1,2),_Dot3OamLoopbackIgnoreRx_Type())
dot3OamLoopbackIgnoreRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamLoopbackIgnoreRx.setStatus(_A)
_Dot3OamStatsTable_Object=MibTable
dot3OamStatsTable=_Dot3OamStatsTable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4))
if mibBuilder.loadTexts:dot3OamStatsTable.setStatus(_A)
_Dot3OamStatsEntry_Object=MibTableRow
dot3OamStatsEntry=_Dot3OamStatsEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1))
dot3OamStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamStatsEntry.setStatus(_A)
_Dot3OamInformationTx_Type=Counter32
_Dot3OamInformationTx_Object=MibTableColumn
dot3OamInformationTx=_Dot3OamInformationTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,1),_Dot3OamInformationTx_Type())
dot3OamInformationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamInformationTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamInformationTx.setUnits(_D)
_Dot3OamInformationRx_Type=Counter32
_Dot3OamInformationRx_Object=MibTableColumn
dot3OamInformationRx=_Dot3OamInformationRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,2),_Dot3OamInformationRx_Type())
dot3OamInformationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamInformationRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamInformationRx.setUnits(_D)
_Dot3OamUniqueEventNotificationTx_Type=Counter32
_Dot3OamUniqueEventNotificationTx_Object=MibTableColumn
dot3OamUniqueEventNotificationTx=_Dot3OamUniqueEventNotificationTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,3),_Dot3OamUniqueEventNotificationTx_Type())
dot3OamUniqueEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationTx.setUnits(_D)
_Dot3OamUniqueEventNotificationRx_Type=Counter32
_Dot3OamUniqueEventNotificationRx_Object=MibTableColumn
dot3OamUniqueEventNotificationRx=_Dot3OamUniqueEventNotificationRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,4),_Dot3OamUniqueEventNotificationRx_Type())
dot3OamUniqueEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationRx.setUnits(_D)
_Dot3OamDuplicateEventNotificationTx_Type=Counter32
_Dot3OamDuplicateEventNotificationTx_Object=MibTableColumn
dot3OamDuplicateEventNotificationTx=_Dot3OamDuplicateEventNotificationTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,5),_Dot3OamDuplicateEventNotificationTx_Type())
dot3OamDuplicateEventNotificationTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationTx.setUnits(_D)
_Dot3OamDuplicateEventNotificationRx_Type=Counter32
_Dot3OamDuplicateEventNotificationRx_Object=MibTableColumn
dot3OamDuplicateEventNotificationRx=_Dot3OamDuplicateEventNotificationRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,6),_Dot3OamDuplicateEventNotificationRx_Type())
dot3OamDuplicateEventNotificationRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationRx.setUnits(_D)
_Dot3OamLoopbackControlTx_Type=Counter32
_Dot3OamLoopbackControlTx_Object=MibTableColumn
dot3OamLoopbackControlTx=_Dot3OamLoopbackControlTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,7),_Dot3OamLoopbackControlTx_Type())
dot3OamLoopbackControlTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamLoopbackControlTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamLoopbackControlTx.setUnits(_D)
_Dot3OamLoopbackControlRx_Type=Counter32
_Dot3OamLoopbackControlRx_Object=MibTableColumn
dot3OamLoopbackControlRx=_Dot3OamLoopbackControlRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,8),_Dot3OamLoopbackControlRx_Type())
dot3OamLoopbackControlRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamLoopbackControlRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamLoopbackControlRx.setUnits(_D)
_Dot3OamVariableRequestTx_Type=Counter32
_Dot3OamVariableRequestTx_Object=MibTableColumn
dot3OamVariableRequestTx=_Dot3OamVariableRequestTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,9),_Dot3OamVariableRequestTx_Type())
dot3OamVariableRequestTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableRequestTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableRequestTx.setUnits(_D)
_Dot3OamVariableRequestRx_Type=Counter32
_Dot3OamVariableRequestRx_Object=MibTableColumn
dot3OamVariableRequestRx=_Dot3OamVariableRequestRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,10),_Dot3OamVariableRequestRx_Type())
dot3OamVariableRequestRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableRequestRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableRequestRx.setUnits(_D)
_Dot3OamVariableResponseTx_Type=Counter32
_Dot3OamVariableResponseTx_Object=MibTableColumn
dot3OamVariableResponseTx=_Dot3OamVariableResponseTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,11),_Dot3OamVariableResponseTx_Type())
dot3OamVariableResponseTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableResponseTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableResponseTx.setUnits(_D)
_Dot3OamVariableResponseRx_Type=Counter32
_Dot3OamVariableResponseRx_Object=MibTableColumn
dot3OamVariableResponseRx=_Dot3OamVariableResponseRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,12),_Dot3OamVariableResponseRx_Type())
dot3OamVariableResponseRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableResponseRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableResponseRx.setUnits(_D)
_Dot3OamOrgSpecificTx_Type=Counter32
_Dot3OamOrgSpecificTx_Object=MibTableColumn
dot3OamOrgSpecificTx=_Dot3OamOrgSpecificTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,13),_Dot3OamOrgSpecificTx_Type())
dot3OamOrgSpecificTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamOrgSpecificTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamOrgSpecificTx.setUnits(_D)
_Dot3OamOrgSpecificRx_Type=Counter32
_Dot3OamOrgSpecificRx_Object=MibTableColumn
dot3OamOrgSpecificRx=_Dot3OamOrgSpecificRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,14),_Dot3OamOrgSpecificRx_Type())
dot3OamOrgSpecificRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamOrgSpecificRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamOrgSpecificRx.setUnits(_D)
_Dot3OamUnsupportedCodesTx_Type=Counter32
_Dot3OamUnsupportedCodesTx_Object=MibTableColumn
dot3OamUnsupportedCodesTx=_Dot3OamUnsupportedCodesTx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,15),_Dot3OamUnsupportedCodesTx_Type())
dot3OamUnsupportedCodesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesTx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesTx.setUnits(_D)
_Dot3OamUnsupportedCodesRx_Type=Counter32
_Dot3OamUnsupportedCodesRx_Object=MibTableColumn
dot3OamUnsupportedCodesRx=_Dot3OamUnsupportedCodesRx_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,16),_Dot3OamUnsupportedCodesRx_Type())
dot3OamUnsupportedCodesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesRx.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesRx.setUnits(_D)
_Dot3OamFramesLostDueToOam_Type=Counter32
_Dot3OamFramesLostDueToOam_Object=MibTableColumn
dot3OamFramesLostDueToOam=_Dot3OamFramesLostDueToOam_Object((1,3,6,1,4,1,3902,1015,1010,1,6,4,1,17),_Dot3OamFramesLostDueToOam_Type())
dot3OamFramesLostDueToOam.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamFramesLostDueToOam.setStatus(_A)
if mibBuilder.loadTexts:dot3OamFramesLostDueToOam.setUnits(_D)
_Dot3OamEventConfigTable_Object=MibTable
dot3OamEventConfigTable=_Dot3OamEventConfigTable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5))
if mibBuilder.loadTexts:dot3OamEventConfigTable.setStatus(_A)
_Dot3OamEventConfigEntry_Object=MibTableRow
dot3OamEventConfigEntry=_Dot3OamEventConfigEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1))
dot3OamEventConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamEventConfigEntry.setStatus(_A)
_Dot3OamErrSymPeriodWindowHi_Type=Unsigned32
_Dot3OamErrSymPeriodWindowHi_Object=MibTableColumn
dot3OamErrSymPeriodWindowHi=_Dot3OamErrSymPeriodWindowHi_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,1),_Dot3OamErrSymPeriodWindowHi_Type())
dot3OamErrSymPeriodWindowHi.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowHi.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowHi.setUnits(_S)
_Dot3OamErrSymPeriodWindowLo_Type=Unsigned32
_Dot3OamErrSymPeriodWindowLo_Object=MibTableColumn
dot3OamErrSymPeriodWindowLo=_Dot3OamErrSymPeriodWindowLo_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,2),_Dot3OamErrSymPeriodWindowLo_Type())
dot3OamErrSymPeriodWindowLo.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowLo.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrSymPeriodWindowLo.setUnits(_T)
_Dot3OamErrSymPeriodThresholdHi_Type=Unsigned32
_Dot3OamErrSymPeriodThresholdHi_Object=MibTableColumn
dot3OamErrSymPeriodThresholdHi=_Dot3OamErrSymPeriodThresholdHi_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,3),_Dot3OamErrSymPeriodThresholdHi_Type())
dot3OamErrSymPeriodThresholdHi.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdHi.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdHi.setUnits(_S)
_Dot3OamErrSymPeriodThresholdLo_Type=Unsigned32
_Dot3OamErrSymPeriodThresholdLo_Object=MibTableColumn
dot3OamErrSymPeriodThresholdLo=_Dot3OamErrSymPeriodThresholdLo_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,4),_Dot3OamErrSymPeriodThresholdLo_Type())
dot3OamErrSymPeriodThresholdLo.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdLo.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrSymPeriodThresholdLo.setUnits(_T)
_Dot3OamErrSymPeriodEvNotifEnable_Type=TruthValue
_Dot3OamErrSymPeriodEvNotifEnable_Object=MibTableColumn
dot3OamErrSymPeriodEvNotifEnable=_Dot3OamErrSymPeriodEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,5),_Dot3OamErrSymPeriodEvNotifEnable_Type())
dot3OamErrSymPeriodEvNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrSymPeriodEvNotifEnable.setStatus(_A)
_Dot3OamErrFramePeriodWindow_Type=Unsigned32
_Dot3OamErrFramePeriodWindow_Object=MibTableColumn
dot3OamErrFramePeriodWindow=_Dot3OamErrFramePeriodWindow_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,6),_Dot3OamErrFramePeriodWindow_Type())
dot3OamErrFramePeriodWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFramePeriodWindow.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrFramePeriodWindow.setUnits(_D)
_Dot3OamErrFramePeriodThreshold_Type=Unsigned32
_Dot3OamErrFramePeriodThreshold_Object=MibTableColumn
dot3OamErrFramePeriodThreshold=_Dot3OamErrFramePeriodThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,7),_Dot3OamErrFramePeriodThreshold_Type())
dot3OamErrFramePeriodThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFramePeriodThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrFramePeriodThreshold.setUnits(_D)
_Dot3OamErrFramePeriodEvNotifEnable_Type=TruthValue
_Dot3OamErrFramePeriodEvNotifEnable_Object=MibTableColumn
dot3OamErrFramePeriodEvNotifEnable=_Dot3OamErrFramePeriodEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,8),_Dot3OamErrFramePeriodEvNotifEnable_Type())
dot3OamErrFramePeriodEvNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFramePeriodEvNotifEnable.setStatus(_A)
_Dot3OamErrFrameWindow_Type=Unsigned32
_Dot3OamErrFrameWindow_Object=MibTableColumn
dot3OamErrFrameWindow=_Dot3OamErrFrameWindow_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,9),_Dot3OamErrFrameWindow_Type())
dot3OamErrFrameWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFrameWindow.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrFrameWindow.setUnits(_U)
_Dot3OamErrFrameThreshold_Type=Unsigned32
_Dot3OamErrFrameThreshold_Object=MibTableColumn
dot3OamErrFrameThreshold=_Dot3OamErrFrameThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,10),_Dot3OamErrFrameThreshold_Type())
dot3OamErrFrameThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFrameThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrFrameThreshold.setUnits(_D)
_Dot3OamErrFrameEvNotifEnable_Type=TruthValue
_Dot3OamErrFrameEvNotifEnable_Object=MibTableColumn
dot3OamErrFrameEvNotifEnable=_Dot3OamErrFrameEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,11),_Dot3OamErrFrameEvNotifEnable_Type())
dot3OamErrFrameEvNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFrameEvNotifEnable.setStatus(_A)
class _Dot3OamErrFrameSecsSummaryWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,9000))
_Dot3OamErrFrameSecsSummaryWindow_Type.__name__=_E
_Dot3OamErrFrameSecsSummaryWindow_Object=MibTableColumn
dot3OamErrFrameSecsSummaryWindow=_Dot3OamErrFrameSecsSummaryWindow_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,12),_Dot3OamErrFrameSecsSummaryWindow_Type())
dot3OamErrFrameSecsSummaryWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryWindow.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryWindow.setUnits(_U)
class _Dot3OamErrFrameSecsSummaryThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_Dot3OamErrFrameSecsSummaryThreshold_Type.__name__=_E
_Dot3OamErrFrameSecsSummaryThreshold_Object=MibTableColumn
dot3OamErrFrameSecsSummaryThreshold=_Dot3OamErrFrameSecsSummaryThreshold_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,13),_Dot3OamErrFrameSecsSummaryThreshold_Type())
dot3OamErrFrameSecsSummaryThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryThreshold.setStatus(_A)
if mibBuilder.loadTexts:dot3OamErrFrameSecsSummaryThreshold.setUnits('errored frame seconds')
_Dot3OamErrFrameSecsEvNotifEnable_Type=TruthValue
_Dot3OamErrFrameSecsEvNotifEnable_Object=MibTableColumn
dot3OamErrFrameSecsEvNotifEnable=_Dot3OamErrFrameSecsEvNotifEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,14),_Dot3OamErrFrameSecsEvNotifEnable_Type())
dot3OamErrFrameSecsEvNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamErrFrameSecsEvNotifEnable.setStatus(_A)
_Dot3OamDyingGaspEnable_Type=TruthValue
_Dot3OamDyingGaspEnable_Object=MibTableColumn
dot3OamDyingGaspEnable=_Dot3OamDyingGaspEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,15),_Dot3OamDyingGaspEnable_Type())
dot3OamDyingGaspEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamDyingGaspEnable.setStatus(_A)
_Dot3OamCriticalEventEnable_Type=TruthValue
_Dot3OamCriticalEventEnable_Object=MibTableColumn
dot3OamCriticalEventEnable=_Dot3OamCriticalEventEnable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,5,1,16),_Dot3OamCriticalEventEnable_Type())
dot3OamCriticalEventEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OamCriticalEventEnable.setStatus(_A)
_Dot3OamEventLogTable_Object=MibTable
dot3OamEventLogTable=_Dot3OamEventLogTable_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6))
if mibBuilder.loadTexts:dot3OamEventLogTable.setStatus(_A)
_Dot3OamEventLogEntry_Object=MibTableRow
dot3OamEventLogEntry=_Dot3OamEventLogEntry_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1))
dot3OamEventLogEntry.setIndexNames((0,_F,_G),(0,_V,_W))
if mibBuilder.loadTexts:dot3OamEventLogEntry.setStatus(_A)
_Dot3OamEventLogIndex_Type=Unsigned32
_Dot3OamEventLogIndex_Object=MibTableColumn
dot3OamEventLogIndex=_Dot3OamEventLogIndex_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,1),_Dot3OamEventLogIndex_Type())
dot3OamEventLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dot3OamEventLogIndex.setStatus(_A)
_Dot3OamEventLogTimestamp_Type=TimeStamp
_Dot3OamEventLogTimestamp_Object=MibTableColumn
dot3OamEventLogTimestamp=_Dot3OamEventLogTimestamp_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,2),_Dot3OamEventLogTimestamp_Type())
dot3OamEventLogTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogTimestamp.setStatus(_A)
_Dot3OamEventLogOui_Type=Dot3Oui
_Dot3OamEventLogOui_Object=MibTableColumn
dot3OamEventLogOui=_Dot3OamEventLogOui_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,3),_Dot3OamEventLogOui_Type())
dot3OamEventLogOui.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogOui.setStatus(_A)
_Dot3OamEventLogType_Type=Unsigned32
_Dot3OamEventLogType_Object=MibTableColumn
dot3OamEventLogType=_Dot3OamEventLogType_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,4),_Dot3OamEventLogType_Type())
dot3OamEventLogType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogType.setStatus(_A)
class _Dot3OamEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_Dot3OamEventLogLocation_Type.__name__=_E
_Dot3OamEventLogLocation_Object=MibTableColumn
dot3OamEventLogLocation=_Dot3OamEventLogLocation_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,5),_Dot3OamEventLogLocation_Type())
dot3OamEventLogLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogLocation.setStatus(_A)
_Dot3OamEventLogWindowHi_Type=Unsigned32
_Dot3OamEventLogWindowHi_Object=MibTableColumn
dot3OamEventLogWindowHi=_Dot3OamEventLogWindowHi_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,6),_Dot3OamEventLogWindowHi_Type())
dot3OamEventLogWindowHi.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogWindowHi.setStatus(_A)
_Dot3OamEventLogWindowLo_Type=Unsigned32
_Dot3OamEventLogWindowLo_Object=MibTableColumn
dot3OamEventLogWindowLo=_Dot3OamEventLogWindowLo_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,7),_Dot3OamEventLogWindowLo_Type())
dot3OamEventLogWindowLo.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogWindowLo.setStatus(_A)
_Dot3OamEventLogThresholdHi_Type=Unsigned32
_Dot3OamEventLogThresholdHi_Object=MibTableColumn
dot3OamEventLogThresholdHi=_Dot3OamEventLogThresholdHi_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,8),_Dot3OamEventLogThresholdHi_Type())
dot3OamEventLogThresholdHi.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogThresholdHi.setStatus(_A)
_Dot3OamEventLogThresholdLo_Type=Unsigned32
_Dot3OamEventLogThresholdLo_Object=MibTableColumn
dot3OamEventLogThresholdLo=_Dot3OamEventLogThresholdLo_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,9),_Dot3OamEventLogThresholdLo_Type())
dot3OamEventLogThresholdLo.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogThresholdLo.setStatus(_A)
_Dot3OamEventLogValue_Type=CounterBasedGauge64
_Dot3OamEventLogValue_Object=MibTableColumn
dot3OamEventLogValue=_Dot3OamEventLogValue_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,10),_Dot3OamEventLogValue_Type())
dot3OamEventLogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogValue.setStatus(_A)
_Dot3OamEventLogRunningTotal_Type=CounterBasedGauge64
_Dot3OamEventLogRunningTotal_Object=MibTableColumn
dot3OamEventLogRunningTotal=_Dot3OamEventLogRunningTotal_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,11),_Dot3OamEventLogRunningTotal_Type())
dot3OamEventLogRunningTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogRunningTotal.setStatus(_A)
_Dot3OamEventLogEventTotal_Type=Unsigned32
_Dot3OamEventLogEventTotal_Object=MibTableColumn
dot3OamEventLogEventTotal=_Dot3OamEventLogEventTotal_Object((1,3,6,1,4,1,3902,1015,1010,1,6,6,1,12),_Dot3OamEventLogEventTotal_Type())
dot3OamEventLogEventTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamEventLogEventTotal.setStatus(_A)
mibBuilder.exportSymbols(_V,**{'Dot3Oui':Dot3Oui,'dot3OamObjects':dot3OamObjects,'dot3OamTable':dot3OamTable,'dot3OamEntry':dot3OamEntry,'dot3OamAdminState':dot3OamAdminState,'dot3OamOperStatus':dot3OamOperStatus,'dot3OamMode':dot3OamMode,'dot3OamMaxOamPduSize':dot3OamMaxOamPduSize,'dot3OamConfigRevision':dot3OamConfigRevision,'dot3OamFunctionsSupported':dot3OamFunctionsSupported,'dot3OamPeerTable':dot3OamPeerTable,'dot3OamPeerEntry':dot3OamPeerEntry,'dot3OamPeerMacAddress':dot3OamPeerMacAddress,'dot3OamPeerVendorOui':dot3OamPeerVendorOui,'dot3OamPeerVendorInfo':dot3OamPeerVendorInfo,'dot3OamPeerMode':dot3OamPeerMode,'dot3OamPeerMaxOamPduSize':dot3OamPeerMaxOamPduSize,'dot3OamPeerConfigRevision':dot3OamPeerConfigRevision,'dot3OamPeerFunctionsSupported':dot3OamPeerFunctionsSupported,'dot3OamLoopbackTable':dot3OamLoopbackTable,'dot3OamLoopbackEntry':dot3OamLoopbackEntry,'dot3OamLoopbackStatus':dot3OamLoopbackStatus,'dot3OamLoopbackIgnoreRx':dot3OamLoopbackIgnoreRx,'dot3OamStatsTable':dot3OamStatsTable,'dot3OamStatsEntry':dot3OamStatsEntry,'dot3OamInformationTx':dot3OamInformationTx,'dot3OamInformationRx':dot3OamInformationRx,'dot3OamUniqueEventNotificationTx':dot3OamUniqueEventNotificationTx,'dot3OamUniqueEventNotificationRx':dot3OamUniqueEventNotificationRx,'dot3OamDuplicateEventNotificationTx':dot3OamDuplicateEventNotificationTx,'dot3OamDuplicateEventNotificationRx':dot3OamDuplicateEventNotificationRx,'dot3OamLoopbackControlTx':dot3OamLoopbackControlTx,'dot3OamLoopbackControlRx':dot3OamLoopbackControlRx,'dot3OamVariableRequestTx':dot3OamVariableRequestTx,'dot3OamVariableRequestRx':dot3OamVariableRequestRx,'dot3OamVariableResponseTx':dot3OamVariableResponseTx,'dot3OamVariableResponseRx':dot3OamVariableResponseRx,'dot3OamOrgSpecificTx':dot3OamOrgSpecificTx,'dot3OamOrgSpecificRx':dot3OamOrgSpecificRx,'dot3OamUnsupportedCodesTx':dot3OamUnsupportedCodesTx,'dot3OamUnsupportedCodesRx':dot3OamUnsupportedCodesRx,'dot3OamFramesLostDueToOam':dot3OamFramesLostDueToOam,'dot3OamEventConfigTable':dot3OamEventConfigTable,'dot3OamEventConfigEntry':dot3OamEventConfigEntry,'dot3OamErrSymPeriodWindowHi':dot3OamErrSymPeriodWindowHi,'dot3OamErrSymPeriodWindowLo':dot3OamErrSymPeriodWindowLo,'dot3OamErrSymPeriodThresholdHi':dot3OamErrSymPeriodThresholdHi,'dot3OamErrSymPeriodThresholdLo':dot3OamErrSymPeriodThresholdLo,'dot3OamErrSymPeriodEvNotifEnable':dot3OamErrSymPeriodEvNotifEnable,'dot3OamErrFramePeriodWindow':dot3OamErrFramePeriodWindow,'dot3OamErrFramePeriodThreshold':dot3OamErrFramePeriodThreshold,'dot3OamErrFramePeriodEvNotifEnable':dot3OamErrFramePeriodEvNotifEnable,'dot3OamErrFrameWindow':dot3OamErrFrameWindow,'dot3OamErrFrameThreshold':dot3OamErrFrameThreshold,'dot3OamErrFrameEvNotifEnable':dot3OamErrFrameEvNotifEnable,'dot3OamErrFrameSecsSummaryWindow':dot3OamErrFrameSecsSummaryWindow,'dot3OamErrFrameSecsSummaryThreshold':dot3OamErrFrameSecsSummaryThreshold,'dot3OamErrFrameSecsEvNotifEnable':dot3OamErrFrameSecsEvNotifEnable,'dot3OamDyingGaspEnable':dot3OamDyingGaspEnable,'dot3OamCriticalEventEnable':dot3OamCriticalEventEnable,'dot3OamEventLogTable':dot3OamEventLogTable,'dot3OamEventLogEntry':dot3OamEventLogEntry,_W:dot3OamEventLogIndex,'dot3OamEventLogTimestamp':dot3OamEventLogTimestamp,'dot3OamEventLogOui':dot3OamEventLogOui,'dot3OamEventLogType':dot3OamEventLogType,'dot3OamEventLogLocation':dot3OamEventLogLocation,'dot3OamEventLogWindowHi':dot3OamEventLogWindowHi,'dot3OamEventLogWindowLo':dot3OamEventLogWindowLo,'dot3OamEventLogThresholdHi':dot3OamEventLogThresholdHi,'dot3OamEventLogThresholdLo':dot3OamEventLogThresholdLo,'dot3OamEventLogValue':dot3OamEventLogValue,'dot3OamEventLogRunningTotal':dot3OamEventLogRunningTotal,'dot3OamEventLogEventTotal':dot3OamEventLogEventTotal})