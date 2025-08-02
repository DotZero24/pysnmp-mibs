_A6='ciscoIpProtocolFilterStatsGroup'
_A5='ciscoIpProtocolFilterGroup2'
_A4='deprecated'
_A3='cippfIpFilterHits'
_A2='cippfIpFilterICMPGroupName'
_A1='cippfIpFilterDstServiceGroupName'
_A0='cippfIpFilterSrcServiceGroupName'
_z='cippfIpFilterProtocolGroupName'
_y='cippfIpFilterDstIPGroupName'
_x='cippfIpFilterSrcIPGroupName'
_w='cippfIpFilterExtLogInterval'
_v='cippfIpFilterExtLogLevel'
_u='cippfIpFilterExtDescription'
_t='cippfIpFilterICMPCode'
_s='cippfIpFilterFragments'
_r='cippfIpFilterTCPEstablished'
_q='cippfIpFilterICMPType'
_p='cippfIpFilterStatus'
_o='cippfIpFilterLogEnabled'
_n='cippfIpFilterTos'
_m='cippfIpFilterPrecedence'
_l='cippfIpFilterDestPortHigh'
_k='cippfIpFilterDestPortLow'
_j='cippfIpFilterSrcPortHigh'
_i='cippfIpFilterSrcPortLow'
_h='cippfIpFilterProtocol'
_g='cippfIpFilterDestMask'
_f='cippfIpFilterDestAddress'
_e='cippfIpFilterSrcMask'
_d='cippfIpFilterSrcAddress'
_c='cippfIpFilterAddressType'
_b='cippfIpFilterAction'
_a='cippfIpFilterOrderPosition'
_Z='cippfIfIpProfileStatus'
_Y='cippfIfIpProfileName'
_X='cippfIpProfileStatus'
_W='cippfIpProfileLastFilterIndex'
_V='cippfIpProfileType'
_U='cippfIpFilterExtEntry'
_T='ffffffff'
_S='cippfIfIpProfileDirection'
_R='read-only'
_Q='SnmpAdminString'
_P='ifIndex'
_O='IF-MIB'
_N='SyslogSeverity'
_M='cippfIpFilterIndex'
_L='not-accessible'
_K='ciscoIpProtocolFilteringGroup'
_J='cippfIpProfileName'
_I='TruthValue'
_H='Unsigned32'
_G='InetPortNumber'
_F='InetAddress'
_E='CfgFilterGroupName'
_D='Integer32'
_C='read-create'
_B='CISCO-IP-PROTOCOL-FILTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfgFilterGroupName,=mibBuilder.importSymbols('CISCO-FILTER-GROUP-MIB',_E)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SyslogSeverity,=mibBuilder.importSymbols('CISCO-SYSLOG-MIB',_N)
ifIndex,=mibBuilder.importSymbols(_O,_P)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType',_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
ciscoIpProtocolMIB=ModuleIdentity((1,3,6,1,4,1,9,9,278))
if mibBuilder.loadTexts:ciscoIpProtocolMIB.setRevisions(('2005-04-20 00:00','2003-06-16 00:00','2002-07-11 00:00'))
class CippfIpFilterProfileName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CiscoIpProtocolFilterMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpProtocolFilterMIBNotifs=_CiscoIpProtocolFilterMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,278,0))
_CiscoIpProtocolFilterMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpProtocolFilterMIBObjects=_CiscoIpProtocolFilterMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,278,1))
_CippfIpFilterConfig_ObjectIdentity=ObjectIdentity
cippfIpFilterConfig=_CippfIpFilterConfig_ObjectIdentity((1,3,6,1,4,1,9,9,278,1,1))
_CippfIpProfileTable_Object=MibTable
cippfIpProfileTable=_CippfIpProfileTable_Object((1,3,6,1,4,1,9,9,278,1,1,1))
if mibBuilder.loadTexts:cippfIpProfileTable.setStatus(_A)
_CippfIpProfileEntry_Object=MibTableRow
cippfIpProfileEntry=_CippfIpProfileEntry_Object((1,3,6,1,4,1,9,9,278,1,1,1,1))
cippfIpProfileEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cippfIpProfileEntry.setStatus(_A)
_CippfIpProfileName_Type=CippfIpFilterProfileName
_CippfIpProfileName_Object=MibTableColumn
cippfIpProfileName=_CippfIpProfileName_Object((1,3,6,1,4,1,9,9,278,1,1,1,1,1),_CippfIpProfileName_Type())
cippfIpProfileName.setMaxAccess(_L)
if mibBuilder.loadTexts:cippfIpProfileName.setStatus(_A)
class _CippfIpProfileType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('simple',1),('extended',2),('extendedIPv6',3)))
_CippfIpProfileType_Type.__name__=_D
_CippfIpProfileType_Object=MibTableColumn
cippfIpProfileType=_CippfIpProfileType_Object((1,3,6,1,4,1,9,9,278,1,1,1,1,2),_CippfIpProfileType_Type())
cippfIpProfileType.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpProfileType.setStatus(_A)
class _CippfIpProfileLastFilterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CippfIpProfileLastFilterIndex_Type.__name__=_H
_CippfIpProfileLastFilterIndex_Object=MibTableColumn
cippfIpProfileLastFilterIndex=_CippfIpProfileLastFilterIndex_Object((1,3,6,1,4,1,9,9,278,1,1,1,1,3),_CippfIpProfileLastFilterIndex_Type())
cippfIpProfileLastFilterIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:cippfIpProfileLastFilterIndex.setStatus(_A)
_CippfIpProfileStatus_Type=RowStatus
_CippfIpProfileStatus_Object=MibTableColumn
cippfIpProfileStatus=_CippfIpProfileStatus_Object((1,3,6,1,4,1,9,9,278,1,1,1,1,4),_CippfIpProfileStatus_Type())
cippfIpProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpProfileStatus.setStatus(_A)
_CippfIfIpProfileTable_Object=MibTable
cippfIfIpProfileTable=_CippfIfIpProfileTable_Object((1,3,6,1,4,1,9,9,278,1,1,2))
if mibBuilder.loadTexts:cippfIfIpProfileTable.setStatus(_A)
_CippfIfIpProfileEntry_Object=MibTableRow
cippfIfIpProfileEntry=_CippfIfIpProfileEntry_Object((1,3,6,1,4,1,9,9,278,1,1,2,1))
cippfIfIpProfileEntry.setIndexNames((0,_O,_P),(0,_B,_S))
if mibBuilder.loadTexts:cippfIfIpProfileEntry.setStatus(_A)
class _CippfIfIpProfileDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('inboundIPv6',3),('outboundIPv6',4)))
_CippfIfIpProfileDirection_Type.__name__=_D
_CippfIfIpProfileDirection_Object=MibTableColumn
cippfIfIpProfileDirection=_CippfIfIpProfileDirection_Object((1,3,6,1,4,1,9,9,278,1,1,2,1,1),_CippfIfIpProfileDirection_Type())
cippfIfIpProfileDirection.setMaxAccess(_L)
if mibBuilder.loadTexts:cippfIfIpProfileDirection.setStatus(_A)
_CippfIfIpProfileName_Type=CippfIpFilterProfileName
_CippfIfIpProfileName_Object=MibTableColumn
cippfIfIpProfileName=_CippfIfIpProfileName_Object((1,3,6,1,4,1,9,9,278,1,1,2,1,2),_CippfIfIpProfileName_Type())
cippfIfIpProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIfIpProfileName.setStatus(_A)
_CippfIfIpProfileStatus_Type=RowStatus
_CippfIfIpProfileStatus_Object=MibTableColumn
cippfIfIpProfileStatus=_CippfIfIpProfileStatus_Object((1,3,6,1,4,1,9,9,278,1,1,2,1,3),_CippfIfIpProfileStatus_Type())
cippfIfIpProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIfIpProfileStatus.setStatus(_A)
_CippfIpFilterTable_Object=MibTable
cippfIpFilterTable=_CippfIpFilterTable_Object((1,3,6,1,4,1,9,9,278,1,1,3))
if mibBuilder.loadTexts:cippfIpFilterTable.setStatus(_A)
_CippfIpFilterEntry_Object=MibTableRow
cippfIpFilterEntry=_CippfIpFilterEntry_Object((1,3,6,1,4,1,9,9,278,1,1,3,1))
cippfIpFilterEntry.setIndexNames((0,_B,_J),(0,_B,_M))
if mibBuilder.loadTexts:cippfIpFilterEntry.setStatus(_A)
class _CippfIpFilterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CippfIpFilterIndex_Type.__name__=_H
_CippfIpFilterIndex_Object=MibTableColumn
cippfIpFilterIndex=_CippfIpFilterIndex_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,1),_CippfIpFilterIndex_Type())
cippfIpFilterIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cippfIpFilterIndex.setStatus(_A)
class _CippfIpFilterOrderPosition_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CippfIpFilterOrderPosition_Type.__name__=_H
_CippfIpFilterOrderPosition_Object=MibTableColumn
cippfIpFilterOrderPosition=_CippfIpFilterOrderPosition_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,2),_CippfIpFilterOrderPosition_Type())
cippfIpFilterOrderPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterOrderPosition.setStatus(_A)
class _CippfIpFilterAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
_CippfIpFilterAction_Type.__name__=_D
_CippfIpFilterAction_Object=MibTableColumn
cippfIpFilterAction=_CippfIpFilterAction_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,3),_CippfIpFilterAction_Type())
cippfIpFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterAction.setStatus(_A)
_CippfIpFilterAddressType_Type=InetAddressType
_CippfIpFilterAddressType_Object=MibTableColumn
cippfIpFilterAddressType=_CippfIpFilterAddressType_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,4),_CippfIpFilterAddressType_Type())
cippfIpFilterAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterAddressType.setStatus(_A)
class _CippfIpFilterSrcAddress_Type(InetAddress):defaultValue=OctetString('0')
_CippfIpFilterSrcAddress_Type.__name__=_F
_CippfIpFilterSrcAddress_Object=MibTableColumn
cippfIpFilterSrcAddress=_CippfIpFilterSrcAddress_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,5),_CippfIpFilterSrcAddress_Type())
cippfIpFilterSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterSrcAddress.setStatus(_A)
class _CippfIpFilterSrcMask_Type(InetAddress):defaultHexValue=_T
_CippfIpFilterSrcMask_Type.__name__=_F
_CippfIpFilterSrcMask_Object=MibTableColumn
cippfIpFilterSrcMask=_CippfIpFilterSrcMask_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,6),_CippfIpFilterSrcMask_Type())
cippfIpFilterSrcMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterSrcMask.setStatus(_A)
class _CippfIpFilterDestAddress_Type(InetAddress):defaultValue=OctetString('0')
_CippfIpFilterDestAddress_Type.__name__=_F
_CippfIpFilterDestAddress_Object=MibTableColumn
cippfIpFilterDestAddress=_CippfIpFilterDestAddress_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,7),_CippfIpFilterDestAddress_Type())
cippfIpFilterDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterDestAddress.setStatus(_A)
class _CippfIpFilterDestMask_Type(InetAddress):defaultHexValue=_T
_CippfIpFilterDestMask_Type.__name__=_F
_CippfIpFilterDestMask_Object=MibTableColumn
cippfIpFilterDestMask=_CippfIpFilterDestMask_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,8),_CippfIpFilterDestMask_Type())
cippfIpFilterDestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterDestMask.setStatus(_A)
class _CippfIpFilterProtocol_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CippfIpFilterProtocol_Type.__name__=_D
_CippfIpFilterProtocol_Object=MibTableColumn
cippfIpFilterProtocol=_CippfIpFilterProtocol_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,9),_CippfIpFilterProtocol_Type())
cippfIpFilterProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterProtocol.setStatus(_A)
class _CippfIpFilterSrcPortLow_Type(InetPortNumber):defaultValue=0
_CippfIpFilterSrcPortLow_Type.__name__=_G
_CippfIpFilterSrcPortLow_Object=MibTableColumn
cippfIpFilterSrcPortLow=_CippfIpFilterSrcPortLow_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,10),_CippfIpFilterSrcPortLow_Type())
cippfIpFilterSrcPortLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterSrcPortLow.setStatus(_A)
class _CippfIpFilterSrcPortHigh_Type(InetPortNumber):defaultValue=65535
_CippfIpFilterSrcPortHigh_Type.__name__=_G
_CippfIpFilterSrcPortHigh_Object=MibTableColumn
cippfIpFilterSrcPortHigh=_CippfIpFilterSrcPortHigh_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,11),_CippfIpFilterSrcPortHigh_Type())
cippfIpFilterSrcPortHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterSrcPortHigh.setStatus(_A)
class _CippfIpFilterDestPortLow_Type(InetPortNumber):defaultValue=0
_CippfIpFilterDestPortLow_Type.__name__=_G
_CippfIpFilterDestPortLow_Object=MibTableColumn
cippfIpFilterDestPortLow=_CippfIpFilterDestPortLow_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,12),_CippfIpFilterDestPortLow_Type())
cippfIpFilterDestPortLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterDestPortLow.setStatus(_A)
class _CippfIpFilterDestPortHigh_Type(InetPortNumber):defaultValue=65535
_CippfIpFilterDestPortHigh_Type.__name__=_G
_CippfIpFilterDestPortHigh_Object=MibTableColumn
cippfIpFilterDestPortHigh=_CippfIpFilterDestPortHigh_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,13),_CippfIpFilterDestPortHigh_Type())
cippfIpFilterDestPortHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterDestPortHigh.setStatus(_A)
class _CippfIpFilterPrecedence_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('any',-1),('routine',0),('priority',1),('immediate',2),('flash',3),('flashOverride',4),('critical',5),('internet',6),('network',7)))
_CippfIpFilterPrecedence_Type.__name__=_D
_CippfIpFilterPrecedence_Object=MibTableColumn
cippfIpFilterPrecedence=_CippfIpFilterPrecedence_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,14),_CippfIpFilterPrecedence_Type())
cippfIpFilterPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterPrecedence.setStatus(_A)
class _CippfIpFilterTos_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_CippfIpFilterTos_Type.__name__=_D
_CippfIpFilterTos_Object=MibTableColumn
cippfIpFilterTos=_CippfIpFilterTos_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,15),_CippfIpFilterTos_Type())
cippfIpFilterTos.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterTos.setStatus(_A)
class _CippfIpFilterLogEnabled_Type(TruthValue):defaultValue=2
_CippfIpFilterLogEnabled_Type.__name__=_I
_CippfIpFilterLogEnabled_Object=MibTableColumn
cippfIpFilterLogEnabled=_CippfIpFilterLogEnabled_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,16),_CippfIpFilterLogEnabled_Type())
cippfIpFilterLogEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterLogEnabled.setStatus(_A)
_CippfIpFilterStatus_Type=RowStatus
_CippfIpFilterStatus_Object=MibTableColumn
cippfIpFilterStatus=_CippfIpFilterStatus_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,17),_CippfIpFilterStatus_Type())
cippfIpFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterStatus.setStatus(_A)
class _CippfIpFilterICMPType_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CippfIpFilterICMPType_Type.__name__=_D
_CippfIpFilterICMPType_Object=MibTableColumn
cippfIpFilterICMPType=_CippfIpFilterICMPType_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,18),_CippfIpFilterICMPType_Type())
cippfIpFilterICMPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterICMPType.setStatus(_A)
class _CippfIpFilterTCPEstablished_Type(TruthValue):defaultValue=2
_CippfIpFilterTCPEstablished_Type.__name__=_I
_CippfIpFilterTCPEstablished_Object=MibTableColumn
cippfIpFilterTCPEstablished=_CippfIpFilterTCPEstablished_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,19),_CippfIpFilterTCPEstablished_Type())
cippfIpFilterTCPEstablished.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterTCPEstablished.setStatus(_A)
class _CippfIpFilterFragments_Type(TruthValue):defaultValue=2
_CippfIpFilterFragments_Type.__name__=_I
_CippfIpFilterFragments_Object=MibTableColumn
cippfIpFilterFragments=_CippfIpFilterFragments_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,20),_CippfIpFilterFragments_Type())
cippfIpFilterFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterFragments.setStatus(_A)
class _CippfIpFilterICMPCode_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CippfIpFilterICMPCode_Type.__name__=_D
_CippfIpFilterICMPCode_Object=MibTableColumn
cippfIpFilterICMPCode=_CippfIpFilterICMPCode_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,21),_CippfIpFilterICMPCode_Type())
cippfIpFilterICMPCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterICMPCode.setStatus(_A)
class _CippfIpFilterSrcIPGroupName_Type(CfgFilterGroupName):defaultValue=OctetString('')
_CippfIpFilterSrcIPGroupName_Type.__name__=_E
_CippfIpFilterSrcIPGroupName_Object=MibTableColumn
cippfIpFilterSrcIPGroupName=_CippfIpFilterSrcIPGroupName_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,22),_CippfIpFilterSrcIPGroupName_Type())
cippfIpFilterSrcIPGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterSrcIPGroupName.setStatus(_A)
class _CippfIpFilterDstIPGroupName_Type(CfgFilterGroupName):defaultValue=OctetString('')
_CippfIpFilterDstIPGroupName_Type.__name__=_E
_CippfIpFilterDstIPGroupName_Object=MibTableColumn
cippfIpFilterDstIPGroupName=_CippfIpFilterDstIPGroupName_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,23),_CippfIpFilterDstIPGroupName_Type())
cippfIpFilterDstIPGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterDstIPGroupName.setStatus(_A)
class _CippfIpFilterProtocolGroupName_Type(CfgFilterGroupName):defaultValue=OctetString('')
_CippfIpFilterProtocolGroupName_Type.__name__=_E
_CippfIpFilterProtocolGroupName_Object=MibTableColumn
cippfIpFilterProtocolGroupName=_CippfIpFilterProtocolGroupName_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,24),_CippfIpFilterProtocolGroupName_Type())
cippfIpFilterProtocolGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterProtocolGroupName.setStatus(_A)
class _CippfIpFilterSrcServiceGroupName_Type(CfgFilterGroupName):defaultValue=OctetString('')
_CippfIpFilterSrcServiceGroupName_Type.__name__=_E
_CippfIpFilterSrcServiceGroupName_Object=MibTableColumn
cippfIpFilterSrcServiceGroupName=_CippfIpFilterSrcServiceGroupName_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,25),_CippfIpFilterSrcServiceGroupName_Type())
cippfIpFilterSrcServiceGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterSrcServiceGroupName.setStatus(_A)
class _CippfIpFilterDstServiceGroupName_Type(CfgFilterGroupName):defaultValue=OctetString('')
_CippfIpFilterDstServiceGroupName_Type.__name__=_E
_CippfIpFilterDstServiceGroupName_Object=MibTableColumn
cippfIpFilterDstServiceGroupName=_CippfIpFilterDstServiceGroupName_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,26),_CippfIpFilterDstServiceGroupName_Type())
cippfIpFilterDstServiceGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterDstServiceGroupName.setStatus(_A)
class _CippfIpFilterICMPGroupName_Type(CfgFilterGroupName):defaultValue=OctetString('')
_CippfIpFilterICMPGroupName_Type.__name__=_E
_CippfIpFilterICMPGroupName_Object=MibTableColumn
cippfIpFilterICMPGroupName=_CippfIpFilterICMPGroupName_Object((1,3,6,1,4,1,9,9,278,1,1,3,1,27),_CippfIpFilterICMPGroupName_Type())
cippfIpFilterICMPGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterICMPGroupName.setStatus(_A)
_CippfIpFilterExtTable_Object=MibTable
cippfIpFilterExtTable=_CippfIpFilterExtTable_Object((1,3,6,1,4,1,9,9,278,1,1,4))
if mibBuilder.loadTexts:cippfIpFilterExtTable.setStatus(_A)
_CippfIpFilterExtEntry_Object=MibTableRow
cippfIpFilterExtEntry=_CippfIpFilterExtEntry_Object((1,3,6,1,4,1,9,9,278,1,1,4,1))
if mibBuilder.loadTexts:cippfIpFilterExtEntry.setStatus(_A)
class _CippfIpFilterExtDescription_Type(SnmpAdminString):defaultValue=OctetString('')
_CippfIpFilterExtDescription_Type.__name__=_Q
_CippfIpFilterExtDescription_Object=MibTableColumn
cippfIpFilterExtDescription=_CippfIpFilterExtDescription_Object((1,3,6,1,4,1,9,9,278,1,1,4,1,1),_CippfIpFilterExtDescription_Type())
cippfIpFilterExtDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterExtDescription.setStatus(_A)
class _CippfIpFilterExtLogLevel_Type(SyslogSeverity):defaultValue=7
_CippfIpFilterExtLogLevel_Type.__name__=_N
_CippfIpFilterExtLogLevel_Object=MibTableColumn
cippfIpFilterExtLogLevel=_CippfIpFilterExtLogLevel_Object((1,3,6,1,4,1,9,9,278,1,1,4,1,2),_CippfIpFilterExtLogLevel_Type())
cippfIpFilterExtLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterExtLogLevel.setStatus(_A)
class _CippfIpFilterExtLogInterval_Type(Unsigned32):defaultValue=300
_CippfIpFilterExtLogInterval_Type.__name__=_H
_CippfIpFilterExtLogInterval_Object=MibTableColumn
cippfIpFilterExtLogInterval=_CippfIpFilterExtLogInterval_Object((1,3,6,1,4,1,9,9,278,1,1,4,1,3),_CippfIpFilterExtLogInterval_Type())
cippfIpFilterExtLogInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cippfIpFilterExtLogInterval.setStatus(_A)
if mibBuilder.loadTexts:cippfIpFilterExtLogInterval.setUnits('seconds')
_CippfIpFilterStats_ObjectIdentity=ObjectIdentity
cippfIpFilterStats=_CippfIpFilterStats_ObjectIdentity((1,3,6,1,4,1,9,9,278,1,2))
_CippfIpFilterStatsTable_Object=MibTable
cippfIpFilterStatsTable=_CippfIpFilterStatsTable_Object((1,3,6,1,4,1,9,9,278,1,2,1))
if mibBuilder.loadTexts:cippfIpFilterStatsTable.setStatus(_A)
_CippfIpFilterStatsEntry_Object=MibTableRow
cippfIpFilterStatsEntry=_CippfIpFilterStatsEntry_Object((1,3,6,1,4,1,9,9,278,1,2,1,1))
cippfIpFilterStatsEntry.setIndexNames((0,_B,_J),(0,_B,_M))
if mibBuilder.loadTexts:cippfIpFilterStatsEntry.setStatus(_A)
_CippfIpFilterHits_Type=Counter64
_CippfIpFilterHits_Object=MibTableColumn
cippfIpFilterHits=_CippfIpFilterHits_Object((1,3,6,1,4,1,9,9,278,1,2,1,1,1),_CippfIpFilterHits_Type())
cippfIpFilterHits.setMaxAccess(_R)
if mibBuilder.loadTexts:cippfIpFilterHits.setStatus(_A)
_CiscoIpProtocolFilterMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpProtocolFilterMIBConform=_CiscoIpProtocolFilterMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,278,2))
_CiscoIpProtocolFilterMIBCompl_ObjectIdentity=ObjectIdentity
ciscoIpProtocolFilterMIBCompl=_CiscoIpProtocolFilterMIBCompl_ObjectIdentity((1,3,6,1,4,1,9,9,278,2,1))
_CiscoIpProtocolFilterMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpProtocolFilterMIBGroups=_CiscoIpProtocolFilterMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,278,2,2))
cippfIpFilterEntry.registerAugmentions((_B,_U))
cippfIpFilterExtEntry.setIndexNames(*cippfIpFilterEntry.getIndexNames())
ciscoIpProtocolFilteringGroup=ObjectGroup((1,3,6,1,4,1,9,9,278,2,2,1))
ciscoIpProtocolFilteringGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ciscoIpProtocolFilteringGroup.setStatus(_A)
ciscoIpProtocolFilterGroup2=ObjectGroup((1,3,6,1,4,1,9,9,278,2,2,2))
ciscoIpProtocolFilterGroup2.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoIpProtocolFilterGroup2.setStatus(_A)
ciscoIpProtocolFilterExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,278,2,2,4))
ciscoIpProtocolFilterExtGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ciscoIpProtocolFilterExtGroup.setStatus(_A)
ciscoIpProtocolFilterObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,278,2,2,5))
ciscoIpProtocolFilterObjectGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoIpProtocolFilterObjectGroup.setStatus(_A)
ciscoIpProtocolFilterStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,278,2,2,6))
ciscoIpProtocolFilterStatsGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:ciscoIpProtocolFilterStatsGroup.setStatus(_A)
ciscoIpProtocolMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,278,2,1,1))
ciscoIpProtocolMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoIpProtocolMIBCompliance.setStatus(_A4)
ciscoIpProtocolMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,278,2,1,2))
ciscoIpProtocolMIBComplianceRev1.setObjects(*((_B,_K),(_B,_A5)))
if mibBuilder.loadTexts:ciscoIpProtocolMIBComplianceRev1.setStatus(_A4)
ciscoIpProtocolMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,278,2,1,3))
ciscoIpProtocolMIBComplianceRev2.setObjects(*((_B,_K),(_B,_A6)))
if mibBuilder.loadTexts:ciscoIpProtocolMIBComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CippfIpFilterProfileName':CippfIpFilterProfileName,'ciscoIpProtocolMIB':ciscoIpProtocolMIB,'ciscoIpProtocolFilterMIBNotifs':ciscoIpProtocolFilterMIBNotifs,'ciscoIpProtocolFilterMIBObjects':ciscoIpProtocolFilterMIBObjects,'cippfIpFilterConfig':cippfIpFilterConfig,'cippfIpProfileTable':cippfIpProfileTable,'cippfIpProfileEntry':cippfIpProfileEntry,_J:cippfIpProfileName,_V:cippfIpProfileType,_W:cippfIpProfileLastFilterIndex,_X:cippfIpProfileStatus,'cippfIfIpProfileTable':cippfIfIpProfileTable,'cippfIfIpProfileEntry':cippfIfIpProfileEntry,_S:cippfIfIpProfileDirection,_Y:cippfIfIpProfileName,_Z:cippfIfIpProfileStatus,'cippfIpFilterTable':cippfIpFilterTable,'cippfIpFilterEntry':cippfIpFilterEntry,_M:cippfIpFilterIndex,_a:cippfIpFilterOrderPosition,_b:cippfIpFilterAction,_c:cippfIpFilterAddressType,_d:cippfIpFilterSrcAddress,_e:cippfIpFilterSrcMask,_f:cippfIpFilterDestAddress,_g:cippfIpFilterDestMask,_h:cippfIpFilterProtocol,_i:cippfIpFilterSrcPortLow,_j:cippfIpFilterSrcPortHigh,_k:cippfIpFilterDestPortLow,_l:cippfIpFilterDestPortHigh,_m:cippfIpFilterPrecedence,_n:cippfIpFilterTos,_o:cippfIpFilterLogEnabled,_p:cippfIpFilterStatus,_q:cippfIpFilterICMPType,_r:cippfIpFilterTCPEstablished,_s:cippfIpFilterFragments,_t:cippfIpFilterICMPCode,_x:cippfIpFilterSrcIPGroupName,_y:cippfIpFilterDstIPGroupName,_z:cippfIpFilterProtocolGroupName,_A0:cippfIpFilterSrcServiceGroupName,_A1:cippfIpFilterDstServiceGroupName,_A2:cippfIpFilterICMPGroupName,'cippfIpFilterExtTable':cippfIpFilterExtTable,_U:cippfIpFilterExtEntry,_u:cippfIpFilterExtDescription,_v:cippfIpFilterExtLogLevel,_w:cippfIpFilterExtLogInterval,'cippfIpFilterStats':cippfIpFilterStats,'cippfIpFilterStatsTable':cippfIpFilterStatsTable,'cippfIpFilterStatsEntry':cippfIpFilterStatsEntry,_A3:cippfIpFilterHits,'ciscoIpProtocolFilterMIBConform':ciscoIpProtocolFilterMIBConform,'ciscoIpProtocolFilterMIBCompl':ciscoIpProtocolFilterMIBCompl,'ciscoIpProtocolMIBCompliance':ciscoIpProtocolMIBCompliance,'ciscoIpProtocolMIBComplianceRev1':ciscoIpProtocolMIBComplianceRev1,'ciscoIpProtocolMIBComplianceRev2':ciscoIpProtocolMIBComplianceRev2,'ciscoIpProtocolFilterMIBGroups':ciscoIpProtocolFilterMIBGroups,_K:ciscoIpProtocolFilteringGroup,_A5:ciscoIpProtocolFilterGroup2,'ciscoIpProtocolFilterExtGroup':ciscoIpProtocolFilterExtGroup,'ciscoIpProtocolFilterObjectGroup':ciscoIpProtocolFilterObjectGroup,_A6:ciscoIpProtocolFilterStatsGroup})