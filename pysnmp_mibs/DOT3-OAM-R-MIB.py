_Q='variableSupport'
_P='eventSupport'
_O='loopbackSupport'
_N='unidirectionalSupport'
_M='octets'
_L='passive'
_K='active'
_J='read-write'
_I='disabled'
_H='Bits'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='Integer32'
_C='frames'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_H,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
dot3OamMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,7))
if mibBuilder.loadTexts:dot3OamMIBR.setRevisions(('2006-03-05 00:00',))
class Dot3Oui(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_RadExperimental_ObjectIdentity=ObjectIdentity
radExperimental=_RadExperimental_ObjectIdentity((1,3,6,1,4,1,164,20))
_Dot3OamObjectsR_ObjectIdentity=ObjectIdentity
dot3OamObjectsR=_Dot3OamObjectsR_ObjectIdentity((1,3,6,1,4,1,164,20,7,1))
_Dot3OamTableR_Object=MibTable
dot3OamTableR=_Dot3OamTableR_Object((1,3,6,1,4,1,164,20,7,1,1))
if mibBuilder.loadTexts:dot3OamTableR.setStatus(_A)
_Dot3OamEntryR_Object=MibTableRow
dot3OamEntryR=_Dot3OamEntryR_Object((1,3,6,1,4,1,164,20,7,1,1,1))
dot3OamEntryR.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamEntryR.setStatus(_A)
class _Dot3OamAdminStateR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('enabled',2)))
_Dot3OamAdminStateR_Type.__name__=_D
_Dot3OamAdminStateR_Object=MibTableColumn
dot3OamAdminStateR=_Dot3OamAdminStateR_Object((1,3,6,1,4,1,164,20,7,1,1,1,1),_Dot3OamAdminStateR_Type())
dot3OamAdminStateR.setMaxAccess(_J)
if mibBuilder.loadTexts:dot3OamAdminStateR.setStatus(_A)
class _Dot3OamOperStatusR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,1),('linkFault',2),('passiveWait',3),('activeSendLocal',4),('sendLocalAndRemote',5),('sendLocalAndRemoteOk',6),('oamPeeringLocallyRejected',7),('oamPeeringRemotelyRejected',8),('operational',9),('nonOperHalfDuplex',10)))
_Dot3OamOperStatusR_Type.__name__=_D
_Dot3OamOperStatusR_Object=MibTableColumn
dot3OamOperStatusR=_Dot3OamOperStatusR_Object((1,3,6,1,4,1,164,20,7,1,1,1,2),_Dot3OamOperStatusR_Type())
dot3OamOperStatusR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamOperStatusR.setStatus(_A)
class _Dot3OamModeR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Dot3OamModeR_Type.__name__=_D
_Dot3OamModeR_Object=MibTableColumn
dot3OamModeR=_Dot3OamModeR_Object((1,3,6,1,4,1,164,20,7,1,1,1,3),_Dot3OamModeR_Type())
dot3OamModeR.setMaxAccess(_J)
if mibBuilder.loadTexts:dot3OamModeR.setStatus(_A)
class _Dot3OamMaxOamPduSizeR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_Dot3OamMaxOamPduSizeR_Type.__name__=_E
_Dot3OamMaxOamPduSizeR_Object=MibTableColumn
dot3OamMaxOamPduSizeR=_Dot3OamMaxOamPduSizeR_Object((1,3,6,1,4,1,164,20,7,1,1,1,4),_Dot3OamMaxOamPduSizeR_Type())
dot3OamMaxOamPduSizeR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamMaxOamPduSizeR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamMaxOamPduSizeR.setUnits(_M)
class _Dot3OamConfigRevisionR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3OamConfigRevisionR_Type.__name__=_E
_Dot3OamConfigRevisionR_Object=MibTableColumn
dot3OamConfigRevisionR=_Dot3OamConfigRevisionR_Object((1,3,6,1,4,1,164,20,7,1,1,1,5),_Dot3OamConfigRevisionR_Type())
dot3OamConfigRevisionR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamConfigRevisionR.setStatus(_A)
class _Dot3OamFunctionsSupportedR_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_Dot3OamFunctionsSupportedR_Type.__name__=_H
_Dot3OamFunctionsSupportedR_Object=MibTableColumn
dot3OamFunctionsSupportedR=_Dot3OamFunctionsSupportedR_Object((1,3,6,1,4,1,164,20,7,1,1,1,6),_Dot3OamFunctionsSupportedR_Type())
dot3OamFunctionsSupportedR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamFunctionsSupportedR.setStatus(_A)
_Dot3OamPeerTableR_Object=MibTable
dot3OamPeerTableR=_Dot3OamPeerTableR_Object((1,3,6,1,4,1,164,20,7,1,2))
if mibBuilder.loadTexts:dot3OamPeerTableR.setStatus(_A)
_Dot3OamPeerEntryR_Object=MibTableRow
dot3OamPeerEntryR=_Dot3OamPeerEntryR_Object((1,3,6,1,4,1,164,20,7,1,2,1))
dot3OamPeerEntryR.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamPeerEntryR.setStatus(_A)
_Dot3OamPeerMacAddressR_Type=MacAddress
_Dot3OamPeerMacAddressR_Object=MibTableColumn
dot3OamPeerMacAddressR=_Dot3OamPeerMacAddressR_Object((1,3,6,1,4,1,164,20,7,1,2,1,1),_Dot3OamPeerMacAddressR_Type())
dot3OamPeerMacAddressR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerMacAddressR.setStatus(_A)
_Dot3OamPeerVendorOuiR_Type=Dot3Oui
_Dot3OamPeerVendorOuiR_Object=MibTableColumn
dot3OamPeerVendorOuiR=_Dot3OamPeerVendorOuiR_Object((1,3,6,1,4,1,164,20,7,1,2,1,2),_Dot3OamPeerVendorOuiR_Type())
dot3OamPeerVendorOuiR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerVendorOuiR.setStatus(_A)
_Dot3OamPeerVendorInfoR_Type=Unsigned32
_Dot3OamPeerVendorInfoR_Object=MibTableColumn
dot3OamPeerVendorInfoR=_Dot3OamPeerVendorInfoR_Object((1,3,6,1,4,1,164,20,7,1,2,1,3),_Dot3OamPeerVendorInfoR_Type())
dot3OamPeerVendorInfoR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerVendorInfoR.setStatus(_A)
class _Dot3OamPeerModeR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),('unknown',3)))
_Dot3OamPeerModeR_Type.__name__=_D
_Dot3OamPeerModeR_Object=MibTableColumn
dot3OamPeerModeR=_Dot3OamPeerModeR_Object((1,3,6,1,4,1,164,20,7,1,2,1,4),_Dot3OamPeerModeR_Type())
dot3OamPeerModeR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerModeR.setStatus(_A)
class _Dot3OamPeerMaxOamPduSizeR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1518))
_Dot3OamPeerMaxOamPduSizeR_Type.__name__=_E
_Dot3OamPeerMaxOamPduSizeR_Object=MibTableColumn
dot3OamPeerMaxOamPduSizeR=_Dot3OamPeerMaxOamPduSizeR_Object((1,3,6,1,4,1,164,20,7,1,2,1,5),_Dot3OamPeerMaxOamPduSizeR_Type())
dot3OamPeerMaxOamPduSizeR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerMaxOamPduSizeR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamPeerMaxOamPduSizeR.setUnits(_M)
class _Dot3OamPeerConfigRevisionR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot3OamPeerConfigRevisionR_Type.__name__=_E
_Dot3OamPeerConfigRevisionR_Object=MibTableColumn
dot3OamPeerConfigRevisionR=_Dot3OamPeerConfigRevisionR_Object((1,3,6,1,4,1,164,20,7,1,2,1,6),_Dot3OamPeerConfigRevisionR_Type())
dot3OamPeerConfigRevisionR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerConfigRevisionR.setStatus(_A)
class _Dot3OamPeerFunctionsSupportedR_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_Dot3OamPeerFunctionsSupportedR_Type.__name__=_H
_Dot3OamPeerFunctionsSupportedR_Object=MibTableColumn
dot3OamPeerFunctionsSupportedR=_Dot3OamPeerFunctionsSupportedR_Object((1,3,6,1,4,1,164,20,7,1,2,1,7),_Dot3OamPeerFunctionsSupportedR_Type())
dot3OamPeerFunctionsSupportedR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamPeerFunctionsSupportedR.setStatus(_A)
_Dot3OamStatsTableR_Object=MibTable
dot3OamStatsTableR=_Dot3OamStatsTableR_Object((1,3,6,1,4,1,164,20,7,1,4))
if mibBuilder.loadTexts:dot3OamStatsTableR.setStatus(_A)
_Dot3OamStatsEntryR_Object=MibTableRow
dot3OamStatsEntryR=_Dot3OamStatsEntryR_Object((1,3,6,1,4,1,164,20,7,1,4,1))
dot3OamStatsEntryR.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dot3OamStatsEntryR.setStatus(_A)
_Dot3OamInformationTxR_Type=Counter32
_Dot3OamInformationTxR_Object=MibTableColumn
dot3OamInformationTxR=_Dot3OamInformationTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,1),_Dot3OamInformationTxR_Type())
dot3OamInformationTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamInformationTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamInformationTxR.setUnits(_C)
_Dot3OamInformationRxR_Type=Counter32
_Dot3OamInformationRxR_Object=MibTableColumn
dot3OamInformationRxR=_Dot3OamInformationRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,2),_Dot3OamInformationRxR_Type())
dot3OamInformationRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamInformationRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamInformationRxR.setUnits(_C)
_Dot3OamUniqueEventNotificationTxR_Type=Counter32
_Dot3OamUniqueEventNotificationTxR_Object=MibTableColumn
dot3OamUniqueEventNotificationTxR=_Dot3OamUniqueEventNotificationTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,3),_Dot3OamUniqueEventNotificationTxR_Type())
dot3OamUniqueEventNotificationTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationTxR.setUnits(_C)
_Dot3OamUniqueEventNotificationRxR_Type=Counter32
_Dot3OamUniqueEventNotificationRxR_Object=MibTableColumn
dot3OamUniqueEventNotificationRxR=_Dot3OamUniqueEventNotificationRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,4),_Dot3OamUniqueEventNotificationRxR_Type())
dot3OamUniqueEventNotificationRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUniqueEventNotificationRxR.setUnits(_C)
_Dot3OamDuplicateEventNotificationTxR_Type=Counter32
_Dot3OamDuplicateEventNotificationTxR_Object=MibTableColumn
dot3OamDuplicateEventNotificationTxR=_Dot3OamDuplicateEventNotificationTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,5),_Dot3OamDuplicateEventNotificationTxR_Type())
dot3OamDuplicateEventNotificationTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationTxR.setUnits(_C)
_Dot3OamDuplicateEventNotificationRxR_Type=Counter32
_Dot3OamDuplicateEventNotificationRxR_Object=MibTableColumn
dot3OamDuplicateEventNotificationRxR=_Dot3OamDuplicateEventNotificationRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,6),_Dot3OamDuplicateEventNotificationRxR_Type())
dot3OamDuplicateEventNotificationRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamDuplicateEventNotificationRxR.setUnits(_C)
_Dot3OamLoopbackControlTxR_Type=Counter32
_Dot3OamLoopbackControlTxR_Object=MibTableColumn
dot3OamLoopbackControlTxR=_Dot3OamLoopbackControlTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,7),_Dot3OamLoopbackControlTxR_Type())
dot3OamLoopbackControlTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamLoopbackControlTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamLoopbackControlTxR.setUnits(_C)
_Dot3OamLoopbackControlRxR_Type=Counter32
_Dot3OamLoopbackControlRxR_Object=MibTableColumn
dot3OamLoopbackControlRxR=_Dot3OamLoopbackControlRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,8),_Dot3OamLoopbackControlRxR_Type())
dot3OamLoopbackControlRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamLoopbackControlRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamLoopbackControlRxR.setUnits(_C)
_Dot3OamVariableRequestTxR_Type=Counter32
_Dot3OamVariableRequestTxR_Object=MibTableColumn
dot3OamVariableRequestTxR=_Dot3OamVariableRequestTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,9),_Dot3OamVariableRequestTxR_Type())
dot3OamVariableRequestTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableRequestTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableRequestTxR.setUnits(_C)
_Dot3OamVariableRequestRxR_Type=Counter32
_Dot3OamVariableRequestRxR_Object=MibTableColumn
dot3OamVariableRequestRxR=_Dot3OamVariableRequestRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,10),_Dot3OamVariableRequestRxR_Type())
dot3OamVariableRequestRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableRequestRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableRequestRxR.setUnits(_C)
_Dot3OamVariableResponseTxR_Type=Counter32
_Dot3OamVariableResponseTxR_Object=MibTableColumn
dot3OamVariableResponseTxR=_Dot3OamVariableResponseTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,11),_Dot3OamVariableResponseTxR_Type())
dot3OamVariableResponseTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableResponseTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableResponseTxR.setUnits(_C)
_Dot3OamVariableResponseRxR_Type=Counter32
_Dot3OamVariableResponseRxR_Object=MibTableColumn
dot3OamVariableResponseRxR=_Dot3OamVariableResponseRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,12),_Dot3OamVariableResponseRxR_Type())
dot3OamVariableResponseRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamVariableResponseRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamVariableResponseRxR.setUnits(_C)
_Dot3OamOrgSpecificTxR_Type=Counter32
_Dot3OamOrgSpecificTxR_Object=MibTableColumn
dot3OamOrgSpecificTxR=_Dot3OamOrgSpecificTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,13),_Dot3OamOrgSpecificTxR_Type())
dot3OamOrgSpecificTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamOrgSpecificTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamOrgSpecificTxR.setUnits(_C)
_Dot3OamOrgSpecificRxR_Type=Counter32
_Dot3OamOrgSpecificRxR_Object=MibTableColumn
dot3OamOrgSpecificRxR=_Dot3OamOrgSpecificRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,14),_Dot3OamOrgSpecificRxR_Type())
dot3OamOrgSpecificRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamOrgSpecificRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamOrgSpecificRxR.setUnits(_C)
_Dot3OamUnsupportedCodesTxR_Type=Counter32
_Dot3OamUnsupportedCodesTxR_Object=MibTableColumn
dot3OamUnsupportedCodesTxR=_Dot3OamUnsupportedCodesTxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,15),_Dot3OamUnsupportedCodesTxR_Type())
dot3OamUnsupportedCodesTxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesTxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesTxR.setUnits(_C)
_Dot3OamUnsupportedCodesRxR_Type=Counter32
_Dot3OamUnsupportedCodesRxR_Object=MibTableColumn
dot3OamUnsupportedCodesRxR=_Dot3OamUnsupportedCodesRxR_Object((1,3,6,1,4,1,164,20,7,1,4,1,16),_Dot3OamUnsupportedCodesRxR_Type())
dot3OamUnsupportedCodesRxR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesRxR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamUnsupportedCodesRxR.setUnits(_C)
_Dot3OamFramesLostDueToOamR_Type=Counter32
_Dot3OamFramesLostDueToOamR_Object=MibTableColumn
dot3OamFramesLostDueToOamR=_Dot3OamFramesLostDueToOamR_Object((1,3,6,1,4,1,164,20,7,1,4,1,17),_Dot3OamFramesLostDueToOamR_Type())
dot3OamFramesLostDueToOamR.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3OamFramesLostDueToOamR.setStatus(_A)
if mibBuilder.loadTexts:dot3OamFramesLostDueToOamR.setUnits(_C)
mibBuilder.exportSymbols('DOT3-OAM-R-MIB',**{'Dot3Oui':Dot3Oui,'radExperimental':radExperimental,'dot3OamMIBR':dot3OamMIBR,'dot3OamObjectsR':dot3OamObjectsR,'dot3OamTableR':dot3OamTableR,'dot3OamEntryR':dot3OamEntryR,'dot3OamAdminStateR':dot3OamAdminStateR,'dot3OamOperStatusR':dot3OamOperStatusR,'dot3OamModeR':dot3OamModeR,'dot3OamMaxOamPduSizeR':dot3OamMaxOamPduSizeR,'dot3OamConfigRevisionR':dot3OamConfigRevisionR,'dot3OamFunctionsSupportedR':dot3OamFunctionsSupportedR,'dot3OamPeerTableR':dot3OamPeerTableR,'dot3OamPeerEntryR':dot3OamPeerEntryR,'dot3OamPeerMacAddressR':dot3OamPeerMacAddressR,'dot3OamPeerVendorOuiR':dot3OamPeerVendorOuiR,'dot3OamPeerVendorInfoR':dot3OamPeerVendorInfoR,'dot3OamPeerModeR':dot3OamPeerModeR,'dot3OamPeerMaxOamPduSizeR':dot3OamPeerMaxOamPduSizeR,'dot3OamPeerConfigRevisionR':dot3OamPeerConfigRevisionR,'dot3OamPeerFunctionsSupportedR':dot3OamPeerFunctionsSupportedR,'dot3OamStatsTableR':dot3OamStatsTableR,'dot3OamStatsEntryR':dot3OamStatsEntryR,'dot3OamInformationTxR':dot3OamInformationTxR,'dot3OamInformationRxR':dot3OamInformationRxR,'dot3OamUniqueEventNotificationTxR':dot3OamUniqueEventNotificationTxR,'dot3OamUniqueEventNotificationRxR':dot3OamUniqueEventNotificationRxR,'dot3OamDuplicateEventNotificationTxR':dot3OamDuplicateEventNotificationTxR,'dot3OamDuplicateEventNotificationRxR':dot3OamDuplicateEventNotificationRxR,'dot3OamLoopbackControlTxR':dot3OamLoopbackControlTxR,'dot3OamLoopbackControlRxR':dot3OamLoopbackControlRxR,'dot3OamVariableRequestTxR':dot3OamVariableRequestTxR,'dot3OamVariableRequestRxR':dot3OamVariableRequestRxR,'dot3OamVariableResponseTxR':dot3OamVariableResponseTxR,'dot3OamVariableResponseRxR':dot3OamVariableResponseRxR,'dot3OamOrgSpecificTxR':dot3OamOrgSpecificTxR,'dot3OamOrgSpecificRxR':dot3OamOrgSpecificRxR,'dot3OamUnsupportedCodesTxR':dot3OamUnsupportedCodesTxR,'dot3OamUnsupportedCodesRxR':dot3OamUnsupportedCodesRxR,'dot3OamFramesLostDueToOamR':dot3OamFramesLostDueToOamR})