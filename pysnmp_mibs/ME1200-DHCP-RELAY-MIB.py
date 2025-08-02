_b='me1200DhcpRelayControlInfoGroup'
_a='me1200DhcpRelayStatisticsInfoGroup'
_Z='me1200DhcpRelayGlobalsInfoGroup'
_Y='me1200DhcpRelayControlClearStatistics'
_X='me1200DhcpRelayStatisticsDropAgentOption'
_W='me1200DhcpRelayStatisticsKeepAgentOption'
_V='me1200DhcpRelayStatisticsReplaceAgentOption'
_U='me1200DhcpRelayStatisticsReceiveClientAgentOption'
_T='me1200DhcpRelayStatisticsReceiveClientPackets'
_S='me1200DhcpRelayStatisticsReceiveServerPackets'
_R='me1200DhcpRelayStatisticsMissingRemoteId'
_Q='me1200DhcpRelayStatisticsBadRemoteId'
_P='me1200DhcpRelayStatisticsMissingCircuitId'
_O='me1200DhcpRelayStatisticsBadCircuitId'
_N='me1200DhcpRelayStatisticsMissingAgentOption'
_M='me1200DhcpRelayStatisticsAgentOptionErrors'
_L='me1200DhcpRelayStatisticsClientPacketErrors'
_K='me1200DhcpRelayStatisticsClientPacketsRelayed'
_J='me1200DhcpRelayStatisticsServerPacketErrors'
_I='me1200DhcpRelayStatisticsServerPacketsRelayed'
_H='me1200DhcpRelayGlobalsInformationPolicy'
_G='me1200DhcpRelayGlobalsInformationMode'
_F='me1200DhcpRelayGlobalsServerIpAddress'
_E='me1200DhcpRelayGlobalsMode'
_D='read-write'
_C='read-only'
_B='ME1200-DHCP-RELAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200DhcpRelayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,55))
if mibBuilder.loadTexts:me1200DhcpRelayMIB.setRevisions(('2014-04-28 00:00','2014-01-29 00:00','2013-10-29 00:00'))
class ME1200DhcpRelayInformationPolicyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('replace',0),('keep',1),('drop',2)))
_Me1200DhcpRelayMIBObjects_ObjectIdentity=ObjectIdentity
me1200DhcpRelayMIBObjects=_Me1200DhcpRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,1))
_Me1200DhcpRelayConfig_ObjectIdentity=ObjectIdentity
me1200DhcpRelayConfig=_Me1200DhcpRelayConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,1,2))
_Me1200DhcpRelayGlobals_ObjectIdentity=ObjectIdentity
me1200DhcpRelayGlobals=_Me1200DhcpRelayGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,1,2,1))
_Me1200DhcpRelayGlobalsMode_Type=TruthValue
_Me1200DhcpRelayGlobalsMode_Object=MibScalar
me1200DhcpRelayGlobalsMode=_Me1200DhcpRelayGlobalsMode_Object((1,3,6,1,4,1,9,9,815,1,55,1,2,1,1),_Me1200DhcpRelayGlobalsMode_Type())
me1200DhcpRelayGlobalsMode.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200DhcpRelayGlobalsMode.setStatus(_A)
_Me1200DhcpRelayGlobalsServerIpAddress_Type=IpAddress
_Me1200DhcpRelayGlobalsServerIpAddress_Object=MibScalar
me1200DhcpRelayGlobalsServerIpAddress=_Me1200DhcpRelayGlobalsServerIpAddress_Object((1,3,6,1,4,1,9,9,815,1,55,1,2,1,2),_Me1200DhcpRelayGlobalsServerIpAddress_Type())
me1200DhcpRelayGlobalsServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200DhcpRelayGlobalsServerIpAddress.setStatus(_A)
_Me1200DhcpRelayGlobalsInformationMode_Type=TruthValue
_Me1200DhcpRelayGlobalsInformationMode_Object=MibScalar
me1200DhcpRelayGlobalsInformationMode=_Me1200DhcpRelayGlobalsInformationMode_Object((1,3,6,1,4,1,9,9,815,1,55,1,2,1,3),_Me1200DhcpRelayGlobalsInformationMode_Type())
me1200DhcpRelayGlobalsInformationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200DhcpRelayGlobalsInformationMode.setStatus(_A)
_Me1200DhcpRelayGlobalsInformationPolicy_Type=ME1200DhcpRelayInformationPolicyType
_Me1200DhcpRelayGlobalsInformationPolicy_Object=MibScalar
me1200DhcpRelayGlobalsInformationPolicy=_Me1200DhcpRelayGlobalsInformationPolicy_Object((1,3,6,1,4,1,9,9,815,1,55,1,2,1,4),_Me1200DhcpRelayGlobalsInformationPolicy_Type())
me1200DhcpRelayGlobalsInformationPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200DhcpRelayGlobalsInformationPolicy.setStatus(_A)
_Me1200DhcpRelayStatus_ObjectIdentity=ObjectIdentity
me1200DhcpRelayStatus=_Me1200DhcpRelayStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,1,3))
_Me1200DhcpRelayStatistics_ObjectIdentity=ObjectIdentity
me1200DhcpRelayStatistics=_Me1200DhcpRelayStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,1,3,1))
_Me1200DhcpRelayStatisticsServerPacketsRelayed_Type=Unsigned32
_Me1200DhcpRelayStatisticsServerPacketsRelayed_Object=MibScalar
me1200DhcpRelayStatisticsServerPacketsRelayed=_Me1200DhcpRelayStatisticsServerPacketsRelayed_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,1),_Me1200DhcpRelayStatisticsServerPacketsRelayed_Type())
me1200DhcpRelayStatisticsServerPacketsRelayed.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsServerPacketsRelayed.setStatus(_A)
_Me1200DhcpRelayStatisticsServerPacketErrors_Type=Unsigned32
_Me1200DhcpRelayStatisticsServerPacketErrors_Object=MibScalar
me1200DhcpRelayStatisticsServerPacketErrors=_Me1200DhcpRelayStatisticsServerPacketErrors_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,2),_Me1200DhcpRelayStatisticsServerPacketErrors_Type())
me1200DhcpRelayStatisticsServerPacketErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsServerPacketErrors.setStatus(_A)
_Me1200DhcpRelayStatisticsClientPacketsRelayed_Type=Unsigned32
_Me1200DhcpRelayStatisticsClientPacketsRelayed_Object=MibScalar
me1200DhcpRelayStatisticsClientPacketsRelayed=_Me1200DhcpRelayStatisticsClientPacketsRelayed_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,3),_Me1200DhcpRelayStatisticsClientPacketsRelayed_Type())
me1200DhcpRelayStatisticsClientPacketsRelayed.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsClientPacketsRelayed.setStatus(_A)
_Me1200DhcpRelayStatisticsClientPacketErrors_Type=Unsigned32
_Me1200DhcpRelayStatisticsClientPacketErrors_Object=MibScalar
me1200DhcpRelayStatisticsClientPacketErrors=_Me1200DhcpRelayStatisticsClientPacketErrors_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,4),_Me1200DhcpRelayStatisticsClientPacketErrors_Type())
me1200DhcpRelayStatisticsClientPacketErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsClientPacketErrors.setStatus(_A)
_Me1200DhcpRelayStatisticsAgentOptionErrors_Type=Unsigned32
_Me1200DhcpRelayStatisticsAgentOptionErrors_Object=MibScalar
me1200DhcpRelayStatisticsAgentOptionErrors=_Me1200DhcpRelayStatisticsAgentOptionErrors_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,5),_Me1200DhcpRelayStatisticsAgentOptionErrors_Type())
me1200DhcpRelayStatisticsAgentOptionErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsAgentOptionErrors.setStatus(_A)
_Me1200DhcpRelayStatisticsMissingAgentOption_Type=Unsigned32
_Me1200DhcpRelayStatisticsMissingAgentOption_Object=MibScalar
me1200DhcpRelayStatisticsMissingAgentOption=_Me1200DhcpRelayStatisticsMissingAgentOption_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,6),_Me1200DhcpRelayStatisticsMissingAgentOption_Type())
me1200DhcpRelayStatisticsMissingAgentOption.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsMissingAgentOption.setStatus(_A)
_Me1200DhcpRelayStatisticsBadCircuitId_Type=Unsigned32
_Me1200DhcpRelayStatisticsBadCircuitId_Object=MibScalar
me1200DhcpRelayStatisticsBadCircuitId=_Me1200DhcpRelayStatisticsBadCircuitId_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,7),_Me1200DhcpRelayStatisticsBadCircuitId_Type())
me1200DhcpRelayStatisticsBadCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsBadCircuitId.setStatus(_A)
_Me1200DhcpRelayStatisticsMissingCircuitId_Type=Unsigned32
_Me1200DhcpRelayStatisticsMissingCircuitId_Object=MibScalar
me1200DhcpRelayStatisticsMissingCircuitId=_Me1200DhcpRelayStatisticsMissingCircuitId_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,8),_Me1200DhcpRelayStatisticsMissingCircuitId_Type())
me1200DhcpRelayStatisticsMissingCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsMissingCircuitId.setStatus(_A)
_Me1200DhcpRelayStatisticsBadRemoteId_Type=Unsigned32
_Me1200DhcpRelayStatisticsBadRemoteId_Object=MibScalar
me1200DhcpRelayStatisticsBadRemoteId=_Me1200DhcpRelayStatisticsBadRemoteId_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,9),_Me1200DhcpRelayStatisticsBadRemoteId_Type())
me1200DhcpRelayStatisticsBadRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsBadRemoteId.setStatus(_A)
_Me1200DhcpRelayStatisticsMissingRemoteId_Type=Unsigned32
_Me1200DhcpRelayStatisticsMissingRemoteId_Object=MibScalar
me1200DhcpRelayStatisticsMissingRemoteId=_Me1200DhcpRelayStatisticsMissingRemoteId_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,10),_Me1200DhcpRelayStatisticsMissingRemoteId_Type())
me1200DhcpRelayStatisticsMissingRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsMissingRemoteId.setStatus(_A)
_Me1200DhcpRelayStatisticsReceiveServerPackets_Type=Unsigned32
_Me1200DhcpRelayStatisticsReceiveServerPackets_Object=MibScalar
me1200DhcpRelayStatisticsReceiveServerPackets=_Me1200DhcpRelayStatisticsReceiveServerPackets_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,11),_Me1200DhcpRelayStatisticsReceiveServerPackets_Type())
me1200DhcpRelayStatisticsReceiveServerPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsReceiveServerPackets.setStatus(_A)
_Me1200DhcpRelayStatisticsReceiveClientPackets_Type=Unsigned32
_Me1200DhcpRelayStatisticsReceiveClientPackets_Object=MibScalar
me1200DhcpRelayStatisticsReceiveClientPackets=_Me1200DhcpRelayStatisticsReceiveClientPackets_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,12),_Me1200DhcpRelayStatisticsReceiveClientPackets_Type())
me1200DhcpRelayStatisticsReceiveClientPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsReceiveClientPackets.setStatus(_A)
_Me1200DhcpRelayStatisticsReceiveClientAgentOption_Type=Unsigned32
_Me1200DhcpRelayStatisticsReceiveClientAgentOption_Object=MibScalar
me1200DhcpRelayStatisticsReceiveClientAgentOption=_Me1200DhcpRelayStatisticsReceiveClientAgentOption_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,13),_Me1200DhcpRelayStatisticsReceiveClientAgentOption_Type())
me1200DhcpRelayStatisticsReceiveClientAgentOption.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsReceiveClientAgentOption.setStatus(_A)
_Me1200DhcpRelayStatisticsReplaceAgentOption_Type=Unsigned32
_Me1200DhcpRelayStatisticsReplaceAgentOption_Object=MibScalar
me1200DhcpRelayStatisticsReplaceAgentOption=_Me1200DhcpRelayStatisticsReplaceAgentOption_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,14),_Me1200DhcpRelayStatisticsReplaceAgentOption_Type())
me1200DhcpRelayStatisticsReplaceAgentOption.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsReplaceAgentOption.setStatus(_A)
_Me1200DhcpRelayStatisticsKeepAgentOption_Type=Unsigned32
_Me1200DhcpRelayStatisticsKeepAgentOption_Object=MibScalar
me1200DhcpRelayStatisticsKeepAgentOption=_Me1200DhcpRelayStatisticsKeepAgentOption_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,15),_Me1200DhcpRelayStatisticsKeepAgentOption_Type())
me1200DhcpRelayStatisticsKeepAgentOption.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsKeepAgentOption.setStatus(_A)
_Me1200DhcpRelayStatisticsDropAgentOption_Type=Unsigned32
_Me1200DhcpRelayStatisticsDropAgentOption_Object=MibScalar
me1200DhcpRelayStatisticsDropAgentOption=_Me1200DhcpRelayStatisticsDropAgentOption_Object((1,3,6,1,4,1,9,9,815,1,55,1,3,1,16),_Me1200DhcpRelayStatisticsDropAgentOption_Type())
me1200DhcpRelayStatisticsDropAgentOption.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsDropAgentOption.setStatus(_A)
_Me1200DhcpRelayControl_ObjectIdentity=ObjectIdentity
me1200DhcpRelayControl=_Me1200DhcpRelayControl_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,1,4))
_Me1200DhcpRelayControlClearStatistics_Type=TruthValue
_Me1200DhcpRelayControlClearStatistics_Object=MibScalar
me1200DhcpRelayControlClearStatistics=_Me1200DhcpRelayControlClearStatistics_Object((1,3,6,1,4,1,9,9,815,1,55,1,4,1),_Me1200DhcpRelayControlClearStatistics_Type())
me1200DhcpRelayControlClearStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200DhcpRelayControlClearStatistics.setStatus(_A)
_Me1200DhcpRelayMIBConformance_ObjectIdentity=ObjectIdentity
me1200DhcpRelayMIBConformance=_Me1200DhcpRelayMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,2))
_Me1200DhcpRelayMIBCompliances_ObjectIdentity=ObjectIdentity
me1200DhcpRelayMIBCompliances=_Me1200DhcpRelayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,2,1))
_Me1200DhcpRelayMIBGroups_ObjectIdentity=ObjectIdentity
me1200DhcpRelayMIBGroups=_Me1200DhcpRelayMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,55,2,2))
me1200DhcpRelayGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,55,2,2,1))
me1200DhcpRelayGlobalsInfoGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:me1200DhcpRelayGlobalsInfoGroup.setStatus(_A)
me1200DhcpRelayStatisticsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,55,2,2,2))
me1200DhcpRelayStatisticsInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:me1200DhcpRelayStatisticsInfoGroup.setStatus(_A)
me1200DhcpRelayControlInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,55,2,2,3))
me1200DhcpRelayControlInfoGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:me1200DhcpRelayControlInfoGroup.setStatus(_A)
me1200DhcpRelayMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,55,2,1,1))
me1200DhcpRelayMIBCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:me1200DhcpRelayMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200DhcpRelayInformationPolicyType':ME1200DhcpRelayInformationPolicyType,'me1200DhcpRelayMIB':me1200DhcpRelayMIB,'me1200DhcpRelayMIBObjects':me1200DhcpRelayMIBObjects,'me1200DhcpRelayConfig':me1200DhcpRelayConfig,'me1200DhcpRelayGlobals':me1200DhcpRelayGlobals,_E:me1200DhcpRelayGlobalsMode,_F:me1200DhcpRelayGlobalsServerIpAddress,_G:me1200DhcpRelayGlobalsInformationMode,_H:me1200DhcpRelayGlobalsInformationPolicy,'me1200DhcpRelayStatus':me1200DhcpRelayStatus,'me1200DhcpRelayStatistics':me1200DhcpRelayStatistics,_I:me1200DhcpRelayStatisticsServerPacketsRelayed,_J:me1200DhcpRelayStatisticsServerPacketErrors,_K:me1200DhcpRelayStatisticsClientPacketsRelayed,_L:me1200DhcpRelayStatisticsClientPacketErrors,_M:me1200DhcpRelayStatisticsAgentOptionErrors,_N:me1200DhcpRelayStatisticsMissingAgentOption,_O:me1200DhcpRelayStatisticsBadCircuitId,_P:me1200DhcpRelayStatisticsMissingCircuitId,_Q:me1200DhcpRelayStatisticsBadRemoteId,_R:me1200DhcpRelayStatisticsMissingRemoteId,_S:me1200DhcpRelayStatisticsReceiveServerPackets,_T:me1200DhcpRelayStatisticsReceiveClientPackets,_U:me1200DhcpRelayStatisticsReceiveClientAgentOption,_V:me1200DhcpRelayStatisticsReplaceAgentOption,_W:me1200DhcpRelayStatisticsKeepAgentOption,_X:me1200DhcpRelayStatisticsDropAgentOption,'me1200DhcpRelayControl':me1200DhcpRelayControl,_Y:me1200DhcpRelayControlClearStatistics,'me1200DhcpRelayMIBConformance':me1200DhcpRelayMIBConformance,'me1200DhcpRelayMIBCompliances':me1200DhcpRelayMIBCompliances,'me1200DhcpRelayMIBCompliance':me1200DhcpRelayMIBCompliance,'me1200DhcpRelayMIBGroups':me1200DhcpRelayMIBGroups,_Z:me1200DhcpRelayGlobalsInfoGroup,_a:me1200DhcpRelayStatisticsInfoGroup,_b:me1200DhcpRelayControlInfoGroup})