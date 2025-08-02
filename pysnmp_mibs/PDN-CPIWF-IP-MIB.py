_j='pdnCpIwfIpNtfyGroup'
_i='pdnCpIwfIpApplConfigGroup'
_h='pdnCpIwfIpConfigGroup'
_g='pdnCpIwfIpActiveSoftSwitchChanged'
_f='pdnCpIwfIpMgcpRSIPKeepAlive'
_e='pdnCpIwfIpMgcpEndPtFormat'
_d='pdnCpIwfIpMgcpIADomainName'
_c='pdnCpIwfIpMgcpRFC2833LoopSignal'
_b='pdnCpIwfIpMgcpSecAgentDNSIpAddr'
_a='pdnCpIwfIpMgcpSecAgentPortNum'
_Z='pdnCpIwfIpMgcpSecAgentIpAddr'
_Y='pdnCpIwfIpMgcpSecAgentName'
_X='pdnCpIwfIpMgcpPriAgentDNSIpAddr'
_W='pdnCpIwfIpMgcpPriAgentPortNum'
_V='pdnCpIwfIpMgcpPriAgentIpAddr'
_U='pdnCpIwfIpMgcpPriAgentName'
_T='pdnCpIwfIpMgcpPortNumber'
_S='pdnCpIwfIpRtpLocalPortBase'
_R='pdnCpIwfIpActiveSoftswitch'
_Q='pdnCpIwfIpDefGateway'
_P='pdnCpIwfIpNetMask'
_O='pdnCpIwfIpAddress'
_N='pdnCpIwfIpChanTosDSCP'
_M='pdnCpIwfIpChandot1dBasePort'
_L='pdnCpIwfIpMgcpEntry'
_K='pdnCpIwfIpRtpEntry'
_J='pdnCpIwfIpEntry'
_I='pdnCpIwfIpChanType'
_H='read-only'
_G='Unsigned32'
_F='pdnCpIwfIndex'
_E='PDN-CP-IWF-MIB'
_D='Integer32'
_C='read-write'
_B='PDN-CPIWF-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdnCpIwfEntry,pdnCpIwfIndex=mibBuilder.importSymbols(_E,'pdnCpIwfEntry',_F)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,=mibBuilder.importSymbols('PDN-TC','SwitchState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnCpIwfIpMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,53))
if mibBuilder.loadTexts:pdnCpIwfIpMIB.setRevisions(('2005-03-24 11:00','2005-01-05 11:00','2004-12-03 11:00','2004-10-07 11:00','2004-09-30 11:00','2004-08-24 00:00'))
class VoiceChannelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bearer',1),('signaling',2)))
_PdnCpIwfIpNotifications_ObjectIdentity=ObjectIdentity
pdnCpIwfIpNotifications=_PdnCpIwfIpNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,0))
_PdnCpIwfIpMIBObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfIpMIBObjects=_PdnCpIwfIpMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,1))
_PdnCpIwfIpConfigObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfIpConfigObjects=_PdnCpIwfIpConfigObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,1,1))
_PdnCpIwfIpTable_Object=MibTable
pdnCpIwfIpTable=_PdnCpIwfIpTable_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,1))
if mibBuilder.loadTexts:pdnCpIwfIpTable.setStatus(_A)
_PdnCpIwfIpEntry_Object=MibTableRow
pdnCpIwfIpEntry=_PdnCpIwfIpEntry_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,1,1))
if mibBuilder.loadTexts:pdnCpIwfIpEntry.setStatus(_A)
_PdnCpIwfIpAddress_Type=IpAddress
_PdnCpIwfIpAddress_Object=MibTableColumn
pdnCpIwfIpAddress=_PdnCpIwfIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,1,1,1),_PdnCpIwfIpAddress_Type())
pdnCpIwfIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpAddress.setStatus(_A)
_PdnCpIwfIpNetMask_Type=IpAddress
_PdnCpIwfIpNetMask_Object=MibTableColumn
pdnCpIwfIpNetMask=_PdnCpIwfIpNetMask_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,1,1,2),_PdnCpIwfIpNetMask_Type())
pdnCpIwfIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpNetMask.setStatus(_A)
_PdnCpIwfIpDefGateway_Type=IpAddress
_PdnCpIwfIpDefGateway_Object=MibTableColumn
pdnCpIwfIpDefGateway=_PdnCpIwfIpDefGateway_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,1,1,3),_PdnCpIwfIpDefGateway_Type())
pdnCpIwfIpDefGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpDefGateway.setStatus(_A)
class _PdnCpIwfIpActiveSoftswitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('none',3)))
_PdnCpIwfIpActiveSoftswitch_Type.__name__=_D
_PdnCpIwfIpActiveSoftswitch_Object=MibTableColumn
pdnCpIwfIpActiveSoftswitch=_PdnCpIwfIpActiveSoftswitch_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,1,1,4),_PdnCpIwfIpActiveSoftswitch_Type())
pdnCpIwfIpActiveSoftswitch.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnCpIwfIpActiveSoftswitch.setStatus(_A)
_PdnCpIwfIpChanTable_Object=MibTable
pdnCpIwfIpChanTable=_PdnCpIwfIpChanTable_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,2))
if mibBuilder.loadTexts:pdnCpIwfIpChanTable.setStatus(_A)
_PdnCpIwfIpChanEntry_Object=MibTableRow
pdnCpIwfIpChanEntry=_PdnCpIwfIpChanEntry_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,2,1))
pdnCpIwfIpChanEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:pdnCpIwfIpChanEntry.setStatus(_A)
_PdnCpIwfIpChanType_Type=VoiceChannelType
_PdnCpIwfIpChanType_Object=MibTableColumn
pdnCpIwfIpChanType=_PdnCpIwfIpChanType_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,2,1,1),_PdnCpIwfIpChanType_Type())
pdnCpIwfIpChanType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pdnCpIwfIpChanType.setStatus(_A)
class _PdnCpIwfIpChandot1dBasePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PdnCpIwfIpChandot1dBasePort_Type.__name__=_G
_PdnCpIwfIpChandot1dBasePort_Object=MibTableColumn
pdnCpIwfIpChandot1dBasePort=_PdnCpIwfIpChandot1dBasePort_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,2,1,2),_PdnCpIwfIpChandot1dBasePort_Type())
pdnCpIwfIpChandot1dBasePort.setMaxAccess(_H)
if mibBuilder.loadTexts:pdnCpIwfIpChandot1dBasePort.setStatus(_A)
class _PdnCpIwfIpChanTosDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PdnCpIwfIpChanTosDSCP_Type.__name__=_D
_PdnCpIwfIpChanTosDSCP_Object=MibTableColumn
pdnCpIwfIpChanTosDSCP=_PdnCpIwfIpChanTosDSCP_Object((1,3,6,1,4,1,1795,2,24,2,53,1,1,2,1,3),_PdnCpIwfIpChanTosDSCP_Type())
pdnCpIwfIpChanTosDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpChanTosDSCP.setStatus(_A)
_PdnCpIwfIpTestObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfIpTestObjects=_PdnCpIwfIpTestObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,1,2))
_PdnCpIwfIpStatsObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfIpStatsObjects=_PdnCpIwfIpStatsObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,1,3))
_PdnCpIwfIpApplObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfIpApplObjects=_PdnCpIwfIpApplObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,1,4))
_PdnCpIwfIpRtpTable_Object=MibTable
pdnCpIwfIpRtpTable=_PdnCpIwfIpRtpTable_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,1))
if mibBuilder.loadTexts:pdnCpIwfIpRtpTable.setStatus(_A)
_PdnCpIwfIpRtpEntry_Object=MibTableRow
pdnCpIwfIpRtpEntry=_PdnCpIwfIpRtpEntry_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,1,1))
if mibBuilder.loadTexts:pdnCpIwfIpRtpEntry.setStatus(_A)
class _PdnCpIwfIpRtpLocalPortBase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfIpRtpLocalPortBase_Type.__name__=_D
_PdnCpIwfIpRtpLocalPortBase_Object=MibTableColumn
pdnCpIwfIpRtpLocalPortBase=_PdnCpIwfIpRtpLocalPortBase_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,1,1,1),_PdnCpIwfIpRtpLocalPortBase_Type())
pdnCpIwfIpRtpLocalPortBase.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpRtpLocalPortBase.setStatus(_A)
_PdnCpIwfIpMgcpTable_Object=MibTable
pdnCpIwfIpMgcpTable=_PdnCpIwfIpMgcpTable_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2))
if mibBuilder.loadTexts:pdnCpIwfIpMgcpTable.setStatus(_A)
_PdnCpIwfIpMgcpEntry_Object=MibTableRow
pdnCpIwfIpMgcpEntry=_PdnCpIwfIpMgcpEntry_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1))
if mibBuilder.loadTexts:pdnCpIwfIpMgcpEntry.setStatus(_A)
class _PdnCpIwfIpMgcpPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfIpMgcpPortNumber_Type.__name__=_D
_PdnCpIwfIpMgcpPortNumber_Object=MibTableColumn
pdnCpIwfIpMgcpPortNumber=_PdnCpIwfIpMgcpPortNumber_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,1),_PdnCpIwfIpMgcpPortNumber_Type())
pdnCpIwfIpMgcpPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpPortNumber.setStatus(_A)
_PdnCpIwfIpMgcpPriAgentName_Type=DisplayString
_PdnCpIwfIpMgcpPriAgentName_Object=MibTableColumn
pdnCpIwfIpMgcpPriAgentName=_PdnCpIwfIpMgcpPriAgentName_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,2),_PdnCpIwfIpMgcpPriAgentName_Type())
pdnCpIwfIpMgcpPriAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpPriAgentName.setStatus(_A)
_PdnCpIwfIpMgcpPriAgentIpAddr_Type=IpAddress
_PdnCpIwfIpMgcpPriAgentIpAddr_Object=MibTableColumn
pdnCpIwfIpMgcpPriAgentIpAddr=_PdnCpIwfIpMgcpPriAgentIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,3),_PdnCpIwfIpMgcpPriAgentIpAddr_Type())
pdnCpIwfIpMgcpPriAgentIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpPriAgentIpAddr.setStatus(_A)
class _PdnCpIwfIpMgcpPriAgentPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfIpMgcpPriAgentPortNum_Type.__name__=_D
_PdnCpIwfIpMgcpPriAgentPortNum_Object=MibTableColumn
pdnCpIwfIpMgcpPriAgentPortNum=_PdnCpIwfIpMgcpPriAgentPortNum_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,4),_PdnCpIwfIpMgcpPriAgentPortNum_Type())
pdnCpIwfIpMgcpPriAgentPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpPriAgentPortNum.setStatus(_A)
_PdnCpIwfIpMgcpPriAgentDNSIpAddr_Type=IpAddress
_PdnCpIwfIpMgcpPriAgentDNSIpAddr_Object=MibTableColumn
pdnCpIwfIpMgcpPriAgentDNSIpAddr=_PdnCpIwfIpMgcpPriAgentDNSIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,5),_PdnCpIwfIpMgcpPriAgentDNSIpAddr_Type())
pdnCpIwfIpMgcpPriAgentDNSIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpPriAgentDNSIpAddr.setStatus(_A)
_PdnCpIwfIpMgcpSecAgentName_Type=DisplayString
_PdnCpIwfIpMgcpSecAgentName_Object=MibTableColumn
pdnCpIwfIpMgcpSecAgentName=_PdnCpIwfIpMgcpSecAgentName_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,6),_PdnCpIwfIpMgcpSecAgentName_Type())
pdnCpIwfIpMgcpSecAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpSecAgentName.setStatus(_A)
_PdnCpIwfIpMgcpSecAgentIpAddr_Type=IpAddress
_PdnCpIwfIpMgcpSecAgentIpAddr_Object=MibTableColumn
pdnCpIwfIpMgcpSecAgentIpAddr=_PdnCpIwfIpMgcpSecAgentIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,7),_PdnCpIwfIpMgcpSecAgentIpAddr_Type())
pdnCpIwfIpMgcpSecAgentIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpSecAgentIpAddr.setStatus(_A)
class _PdnCpIwfIpMgcpSecAgentPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfIpMgcpSecAgentPortNum_Type.__name__=_D
_PdnCpIwfIpMgcpSecAgentPortNum_Object=MibTableColumn
pdnCpIwfIpMgcpSecAgentPortNum=_PdnCpIwfIpMgcpSecAgentPortNum_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,8),_PdnCpIwfIpMgcpSecAgentPortNum_Type())
pdnCpIwfIpMgcpSecAgentPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpSecAgentPortNum.setStatus(_A)
_PdnCpIwfIpMgcpSecAgentDNSIpAddr_Type=IpAddress
_PdnCpIwfIpMgcpSecAgentDNSIpAddr_Object=MibTableColumn
pdnCpIwfIpMgcpSecAgentDNSIpAddr=_PdnCpIwfIpMgcpSecAgentDNSIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,9),_PdnCpIwfIpMgcpSecAgentDNSIpAddr_Type())
pdnCpIwfIpMgcpSecAgentDNSIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpSecAgentDNSIpAddr.setStatus(_A)
_PdnCpIwfIpMgcpRFC2833LoopSignal_Type=SwitchState
_PdnCpIwfIpMgcpRFC2833LoopSignal_Object=MibTableColumn
pdnCpIwfIpMgcpRFC2833LoopSignal=_PdnCpIwfIpMgcpRFC2833LoopSignal_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,10),_PdnCpIwfIpMgcpRFC2833LoopSignal_Type())
pdnCpIwfIpMgcpRFC2833LoopSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpRFC2833LoopSignal.setStatus(_A)
_PdnCpIwfIpMgcpIADomainName_Type=DisplayString
_PdnCpIwfIpMgcpIADomainName_Object=MibTableColumn
pdnCpIwfIpMgcpIADomainName=_PdnCpIwfIpMgcpIADomainName_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,11),_PdnCpIwfIpMgcpIADomainName_Type())
pdnCpIwfIpMgcpIADomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpIADomainName.setStatus(_A)
class _PdnCpIwfIpMgcpEndPtFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipaddr',1),('bracketandipaddr',2),('domainname',3)))
_PdnCpIwfIpMgcpEndPtFormat_Type.__name__=_D
_PdnCpIwfIpMgcpEndPtFormat_Object=MibTableColumn
pdnCpIwfIpMgcpEndPtFormat=_PdnCpIwfIpMgcpEndPtFormat_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,12),_PdnCpIwfIpMgcpEndPtFormat_Type())
pdnCpIwfIpMgcpEndPtFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpEndPtFormat.setStatus(_A)
class _PdnCpIwfIpMgcpRSIPKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_PdnCpIwfIpMgcpRSIPKeepAlive_Type.__name__=_D
_PdnCpIwfIpMgcpRSIPKeepAlive_Object=MibTableColumn
pdnCpIwfIpMgcpRSIPKeepAlive=_PdnCpIwfIpMgcpRSIPKeepAlive_Object((1,3,6,1,4,1,1795,2,24,2,53,1,4,2,1,13),_PdnCpIwfIpMgcpRSIPKeepAlive_Type())
pdnCpIwfIpMgcpRSIPKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIpMgcpRSIPKeepAlive.setStatus(_A)
_PdnCpIwfIpMIBConformance_ObjectIdentity=ObjectIdentity
pdnCpIwfIpMIBConformance=_PdnCpIwfIpMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,2))
_PdnCpIwfIpMIBCompliances_ObjectIdentity=ObjectIdentity
pdnCpIwfIpMIBCompliances=_PdnCpIwfIpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,2,1))
_PdnCpIwfIpMIBGroups_ObjectIdentity=ObjectIdentity
pdnCpIwfIpMIBGroups=_PdnCpIwfIpMIBGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,2,2))
_PdnCpIwfIpNtfyGroups_ObjectIdentity=ObjectIdentity
pdnCpIwfIpNtfyGroups=_PdnCpIwfIpNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,53,2,3))
pdnCpIwfEntry.registerAugmentions((_B,_J))
pdnCpIwfIpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
pdnCpIwfEntry.registerAugmentions((_B,_K))
pdnCpIwfIpRtpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
pdnCpIwfEntry.registerAugmentions((_B,_L))
pdnCpIwfIpMgcpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
pdnCpIwfIpConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,53,2,2,1))
pdnCpIwfIpConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:pdnCpIwfIpConfigGroup.setStatus(_A)
pdnCpIwfIpApplConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,53,2,2,2))
pdnCpIwfIpApplConfigGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:pdnCpIwfIpApplConfigGroup.setStatus(_A)
pdnCpIwfIpActiveSoftSwitchChanged=NotificationType((1,3,6,1,4,1,1795,2,24,2,53,0,1))
if mibBuilder.loadTexts:pdnCpIwfIpActiveSoftSwitchChanged.setStatus(_A)
pdnCpIwfIpNtfyGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,53,2,3,1))
pdnCpIwfIpNtfyGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:pdnCpIwfIpNtfyGroup.setStatus(_A)
pdnCpIwfIpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,53,2,1,1))
pdnCpIwfIpMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:pdnCpIwfIpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VoiceChannelType':VoiceChannelType,'pdnCpIwfIpMIB':pdnCpIwfIpMIB,'pdnCpIwfIpNotifications':pdnCpIwfIpNotifications,_g:pdnCpIwfIpActiveSoftSwitchChanged,'pdnCpIwfIpMIBObjects':pdnCpIwfIpMIBObjects,'pdnCpIwfIpConfigObjects':pdnCpIwfIpConfigObjects,'pdnCpIwfIpTable':pdnCpIwfIpTable,_J:pdnCpIwfIpEntry,_O:pdnCpIwfIpAddress,_P:pdnCpIwfIpNetMask,_Q:pdnCpIwfIpDefGateway,_R:pdnCpIwfIpActiveSoftswitch,'pdnCpIwfIpChanTable':pdnCpIwfIpChanTable,'pdnCpIwfIpChanEntry':pdnCpIwfIpChanEntry,_I:pdnCpIwfIpChanType,_M:pdnCpIwfIpChandot1dBasePort,_N:pdnCpIwfIpChanTosDSCP,'pdnCpIwfIpTestObjects':pdnCpIwfIpTestObjects,'pdnCpIwfIpStatsObjects':pdnCpIwfIpStatsObjects,'pdnCpIwfIpApplObjects':pdnCpIwfIpApplObjects,'pdnCpIwfIpRtpTable':pdnCpIwfIpRtpTable,_K:pdnCpIwfIpRtpEntry,_S:pdnCpIwfIpRtpLocalPortBase,'pdnCpIwfIpMgcpTable':pdnCpIwfIpMgcpTable,_L:pdnCpIwfIpMgcpEntry,_T:pdnCpIwfIpMgcpPortNumber,_U:pdnCpIwfIpMgcpPriAgentName,_V:pdnCpIwfIpMgcpPriAgentIpAddr,_W:pdnCpIwfIpMgcpPriAgentPortNum,_X:pdnCpIwfIpMgcpPriAgentDNSIpAddr,_Y:pdnCpIwfIpMgcpSecAgentName,_Z:pdnCpIwfIpMgcpSecAgentIpAddr,_a:pdnCpIwfIpMgcpSecAgentPortNum,_b:pdnCpIwfIpMgcpSecAgentDNSIpAddr,_c:pdnCpIwfIpMgcpRFC2833LoopSignal,_d:pdnCpIwfIpMgcpIADomainName,_e:pdnCpIwfIpMgcpEndPtFormat,_f:pdnCpIwfIpMgcpRSIPKeepAlive,'pdnCpIwfIpMIBConformance':pdnCpIwfIpMIBConformance,'pdnCpIwfIpMIBCompliances':pdnCpIwfIpMIBCompliances,'pdnCpIwfIpMIBCompliance':pdnCpIwfIpMIBCompliance,'pdnCpIwfIpMIBGroups':pdnCpIwfIpMIBGroups,_h:pdnCpIwfIpConfigGroup,_i:pdnCpIwfIpApplConfigGroup,'pdnCpIwfIpNtfyGroups':pdnCpIwfIpNtfyGroups,_j:pdnCpIwfIpNtfyGroup})