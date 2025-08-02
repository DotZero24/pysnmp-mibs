_AO='rbnInetIpPoolNotifyGroup'
_AN='rbnInetIpPoolGroup'
_AM='rbnIpPoolNotifyGroupV2'
_AL='rbnIpPoolContextGroup'
_AK='rbnIpPoolInterfaceGroup'
_AJ='rbnIpPoolRangeGroup'
_AI='rbnInetIpPoolCtxLoFallingThrshMet'
_AH='rbnInetIpPoolCtxHiFallingThrshMet'
_AG='rbnInetIpPoolLoFallingThrshMet'
_AF='rbnInetIpPoolHiFallingThrshMet'
_AE='rbnIpPoolContextThresholdPercentageMet'
_AD='rbnInetIpPoolCtxLoFallingNotify'
_AC='rbnInetIpPoolCtxHiFallingNotify'
_AB='rbnInetIpPoolLoFallingNotify'
_AA='rbnInetIpPoolHiFallingNotify'
_A9='rbnInetIpPoolInuse'
_A8='rbnInetIpPoolUnusable'
_A7='rbnIpPoolContextThresholdLogMessage'
_A6='rbnIpPoolContextThresholdSendTrap'
_A5='rbnInetIpPoolCtxPoolType'
_A4='rbnInetIpPoolStartPrefixLen'
_A3='rbnInetIpPoolStartPrefix'
_A2='rbnInetIpPoolStartPrefixType'
_A1='rbnInetIpPoolIfIndex'
_A0='rbnInetIpPoolType'
_z='rbnIpPoolContextThresholdIndex'
_y='rbnIpPoolAddr'
_x='rbnIpPoolInterfaceIdx'
_w='Unsigned32'
_v='Integer32'
_u='rbnIpPoolNameGroup'
_t='rbnIpPoolGroup'
_s='rbnIpPoolContextThresholdMet'
_r='rbnIpPoolThresholdMet'
_q='rbnInetIpPoolCtxLoFallingThrsh'
_p='rbnInetIpPoolCtxHiFallingThrsh'
_o='rbnInetIpPoolLoFallingThrsh'
_n='rbnInetIpPoolHiFallingThrsh'
_m='rbnIpPoolContextThresholdPercentage'
_l='rbnIpPoolContextTotalSize'
_k='rbnIpPoolEndAddr'
_j='rbnIpPoolType'
_i='rbnIpPoolName'
_h='InetAddressPrefixLength'
_g='rbnIpPoolGroupV2'
_f='rbnInetIpPoolCtxThrshType'
_e='rbnInetIpPoolCtxPoolSize'
_d='rbnInetIpPoolCtxAvailable'
_c='rbnInetIpPoolCtxName'
_b='rbnInetIpPoolThrshType'
_a='rbnInetIpPoolAvailable'
_Z='rbnInetIpPoolSize'
_Y='rbnInetIpPoolName'
_X='rbnInetIpPoolInterfaceName'
_W='rbnInetIpPoolEndPrefixLen'
_V='rbnInetIpPoolEndPrefix'
_U='rbnInetIpPoolEndPrefixType'
_T='rbnIpPoolContextLogMessage'
_S='rbnIpPoolContextSendTrap'
_R='rbnIpPoolLogMessage'
_Q='rbnIpPoolSendTrap'
_P='rbnIpPoolInuse'
_O='rbnIpPoolUnusable'
_N='rbnIpPoolSize'
_M='SnmpAdminString'
_L='rbnIpPoolContextThreshold'
_K='rbnIpPoolThreshold'
_J='rbnIpPoolAvailable'
_I='rbnIpPoolMask'
_H='rbnIpPoolInterfaceName'
_G='rbnIpPoolNotifyGroup'
_F='rbnIpPoolContextAvailable'
_E='rbnIpPoolContextName'
_D='not-accessible'
_C='read-only'
_B='current'
_A='RBN-IPPOOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_h,'InetAddressType')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnPercentage,=mibBuilder.importSymbols('RBN-TC','RbnPercentage')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_v,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_w,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rbnIpPoolMib=ModuleIdentity((1,3,6,1,4,1,2352,2,15))
if mibBuilder.loadTexts:rbnIpPoolMib.setRevisions(('2010-02-10 00:00','2005-06-17 00:00','2005-03-14 00:00','2004-09-28 00:00','2001-11-07 17:00'))
class RbnInetPoolType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv6',1),('dhcpv6',2)))
class RbnInetIpPoolThresholdType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('absolute',1),('percentage',2)))
class RbnInetIpPoolThreshold(TextualConvention,Unsigned32):status=_B;displayHint='d'
class RbnInetIpPoolThrshNotify(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('log',1),('trap',2),('both',3)))
_RbnIpPoolMIBNotifications_ObjectIdentity=ObjectIdentity
rbnIpPoolMIBNotifications=_RbnIpPoolMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,15,0))
_RbnIpPoolMIBObjects_ObjectIdentity=ObjectIdentity
rbnIpPoolMIBObjects=_RbnIpPoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,15,1))
_RbnIpPoolTable_Object=MibTable
rbnIpPoolTable=_RbnIpPoolTable_Object((1,3,6,1,4,1,2352,2,15,1,1))
if mibBuilder.loadTexts:rbnIpPoolTable.setStatus(_B)
_RbnIpPoolEntry_Object=MibTableRow
rbnIpPoolEntry=_RbnIpPoolEntry_Object((1,3,6,1,4,1,2352,2,15,1,1,1))
rbnIpPoolEntry.setIndexNames((0,_A,_x),(0,_A,_y))
if mibBuilder.loadTexts:rbnIpPoolEntry.setStatus(_B)
_RbnIpPoolInterfaceIdx_Type=Unsigned32
_RbnIpPoolInterfaceIdx_Object=MibTableColumn
rbnIpPoolInterfaceIdx=_RbnIpPoolInterfaceIdx_Object((1,3,6,1,4,1,2352,2,15,1,1,1,1),_RbnIpPoolInterfaceIdx_Type())
rbnIpPoolInterfaceIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnIpPoolInterfaceIdx.setStatus(_B)
_RbnIpPoolAddr_Type=IpAddress
_RbnIpPoolAddr_Object=MibTableColumn
rbnIpPoolAddr=_RbnIpPoolAddr_Object((1,3,6,1,4,1,2352,2,15,1,1,1,2),_RbnIpPoolAddr_Type())
rbnIpPoolAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnIpPoolAddr.setStatus(_B)
class _RbnIpPoolInterfaceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_RbnIpPoolInterfaceName_Type.__name__=_M
_RbnIpPoolInterfaceName_Object=MibTableColumn
rbnIpPoolInterfaceName=_RbnIpPoolInterfaceName_Object((1,3,6,1,4,1,2352,2,15,1,1,1,3),_RbnIpPoolInterfaceName_Type())
rbnIpPoolInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolInterfaceName.setStatus(_B)
_RbnIpPoolMask_Type=IpAddress
_RbnIpPoolMask_Object=MibTableColumn
rbnIpPoolMask=_RbnIpPoolMask_Object((1,3,6,1,4,1,2352,2,15,1,1,1,4),_RbnIpPoolMask_Type())
rbnIpPoolMask.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolMask.setStatus(_B)
_RbnIpPoolSize_Type=Unsigned32
_RbnIpPoolSize_Object=MibTableColumn
rbnIpPoolSize=_RbnIpPoolSize_Object((1,3,6,1,4,1,2352,2,15,1,1,1,5),_RbnIpPoolSize_Type())
rbnIpPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolSize.setStatus(_B)
_RbnIpPoolAvailable_Type=Unsigned32
_RbnIpPoolAvailable_Object=MibTableColumn
rbnIpPoolAvailable=_RbnIpPoolAvailable_Object((1,3,6,1,4,1,2352,2,15,1,1,1,6),_RbnIpPoolAvailable_Type())
rbnIpPoolAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolAvailable.setStatus(_B)
_RbnIpPoolUnusable_Type=Unsigned32
_RbnIpPoolUnusable_Object=MibTableColumn
rbnIpPoolUnusable=_RbnIpPoolUnusable_Object((1,3,6,1,4,1,2352,2,15,1,1,1,7),_RbnIpPoolUnusable_Type())
rbnIpPoolUnusable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolUnusable.setStatus(_B)
_RbnIpPoolInuse_Type=Unsigned32
_RbnIpPoolInuse_Object=MibTableColumn
rbnIpPoolInuse=_RbnIpPoolInuse_Object((1,3,6,1,4,1,2352,2,15,1,1,1,8),_RbnIpPoolInuse_Type())
rbnIpPoolInuse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolInuse.setStatus(_B)
class _RbnIpPoolThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RbnIpPoolThreshold_Type.__name__=_w
_RbnIpPoolThreshold_Object=MibTableColumn
rbnIpPoolThreshold=_RbnIpPoolThreshold_Object((1,3,6,1,4,1,2352,2,15,1,1,1,9),_RbnIpPoolThreshold_Type())
rbnIpPoolThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolThreshold.setStatus(_B)
_RbnIpPoolSendTrap_Type=TruthValue
_RbnIpPoolSendTrap_Object=MibTableColumn
rbnIpPoolSendTrap=_RbnIpPoolSendTrap_Object((1,3,6,1,4,1,2352,2,15,1,1,1,10),_RbnIpPoolSendTrap_Type())
rbnIpPoolSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolSendTrap.setStatus(_B)
_RbnIpPoolLogMessage_Type=TruthValue
_RbnIpPoolLogMessage_Object=MibTableColumn
rbnIpPoolLogMessage=_RbnIpPoolLogMessage_Object((1,3,6,1,4,1,2352,2,15,1,1,1,11),_RbnIpPoolLogMessage_Type())
rbnIpPoolLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolLogMessage.setStatus(_B)
class _RbnIpPoolName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnIpPoolName_Type.__name__=_M
_RbnIpPoolName_Object=MibTableColumn
rbnIpPoolName=_RbnIpPoolName_Object((1,3,6,1,4,1,2352,2,15,1,1,1,12),_RbnIpPoolName_Type())
rbnIpPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolName.setStatus(_B)
class _RbnIpPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('subnet',0),('range',1)))
_RbnIpPoolType_Type.__name__=_v
_RbnIpPoolType_Object=MibTableColumn
rbnIpPoolType=_RbnIpPoolType_Object((1,3,6,1,4,1,2352,2,15,1,1,1,13),_RbnIpPoolType_Type())
rbnIpPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolType.setStatus(_B)
_RbnIpPoolEndAddr_Type=IpAddress
_RbnIpPoolEndAddr_Object=MibTableColumn
rbnIpPoolEndAddr=_RbnIpPoolEndAddr_Object((1,3,6,1,4,1,2352,2,15,1,1,1,14),_RbnIpPoolEndAddr_Type())
rbnIpPoolEndAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolEndAddr.setStatus(_B)
_RbnIpPoolSummary_ObjectIdentity=ObjectIdentity
rbnIpPoolSummary=_RbnIpPoolSummary_ObjectIdentity((1,3,6,1,4,1,2352,2,15,1,2))
class _RbnIpPoolContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_RbnIpPoolContextName_Type.__name__=_M
_RbnIpPoolContextName_Object=MibScalar
rbnIpPoolContextName=_RbnIpPoolContextName_Object((1,3,6,1,4,1,2352,2,15,1,2,1),_RbnIpPoolContextName_Type())
rbnIpPoolContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextName.setStatus(_B)
_RbnIpPoolContextAvailable_Type=Unsigned32
_RbnIpPoolContextAvailable_Object=MibScalar
rbnIpPoolContextAvailable=_RbnIpPoolContextAvailable_Object((1,3,6,1,4,1,2352,2,15,1,2,2),_RbnIpPoolContextAvailable_Type())
rbnIpPoolContextAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextAvailable.setStatus(_B)
_RbnIpPoolContextThreshold_Type=Unsigned32
_RbnIpPoolContextThreshold_Object=MibScalar
rbnIpPoolContextThreshold=_RbnIpPoolContextThreshold_Object((1,3,6,1,4,1,2352,2,15,1,2,3),_RbnIpPoolContextThreshold_Type())
rbnIpPoolContextThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextThreshold.setStatus(_B)
_RbnIpPoolContextSendTrap_Type=TruthValue
_RbnIpPoolContextSendTrap_Object=MibScalar
rbnIpPoolContextSendTrap=_RbnIpPoolContextSendTrap_Object((1,3,6,1,4,1,2352,2,15,1,2,4),_RbnIpPoolContextSendTrap_Type())
rbnIpPoolContextSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextSendTrap.setStatus(_B)
_RbnIpPoolContextLogMessage_Type=TruthValue
_RbnIpPoolContextLogMessage_Object=MibScalar
rbnIpPoolContextLogMessage=_RbnIpPoolContextLogMessage_Object((1,3,6,1,4,1,2352,2,15,1,2,5),_RbnIpPoolContextLogMessage_Type())
rbnIpPoolContextLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextLogMessage.setStatus(_B)
_RbnIpPoolContextTotalSize_Type=Unsigned32
_RbnIpPoolContextTotalSize_Object=MibScalar
rbnIpPoolContextTotalSize=_RbnIpPoolContextTotalSize_Object((1,3,6,1,4,1,2352,2,15,1,2,6),_RbnIpPoolContextTotalSize_Type())
rbnIpPoolContextTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextTotalSize.setStatus(_B)
_RbnIpPoolContextThresholdPercentTable_Object=MibTable
rbnIpPoolContextThresholdPercentTable=_RbnIpPoolContextThresholdPercentTable_Object((1,3,6,1,4,1,2352,2,15,1,2,7))
if mibBuilder.loadTexts:rbnIpPoolContextThresholdPercentTable.setStatus(_B)
_RbnIpPoolContextThresholdPercentEntry_Object=MibTableRow
rbnIpPoolContextThresholdPercentEntry=_RbnIpPoolContextThresholdPercentEntry_Object((1,3,6,1,4,1,2352,2,15,1,2,7,1))
rbnIpPoolContextThresholdPercentEntry.setIndexNames((0,_A,_z))
if mibBuilder.loadTexts:rbnIpPoolContextThresholdPercentEntry.setStatus(_B)
_RbnIpPoolContextThresholdIndex_Type=Unsigned32
_RbnIpPoolContextThresholdIndex_Object=MibTableColumn
rbnIpPoolContextThresholdIndex=_RbnIpPoolContextThresholdIndex_Object((1,3,6,1,4,1,2352,2,15,1,2,7,1,1),_RbnIpPoolContextThresholdIndex_Type())
rbnIpPoolContextThresholdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnIpPoolContextThresholdIndex.setStatus(_B)
_RbnIpPoolContextThresholdPercentage_Type=RbnPercentage
_RbnIpPoolContextThresholdPercentage_Object=MibTableColumn
rbnIpPoolContextThresholdPercentage=_RbnIpPoolContextThresholdPercentage_Object((1,3,6,1,4,1,2352,2,15,1,2,7,1,2),_RbnIpPoolContextThresholdPercentage_Type())
rbnIpPoolContextThresholdPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextThresholdPercentage.setStatus(_B)
_RbnIpPoolContextThresholdSendTrap_Type=TruthValue
_RbnIpPoolContextThresholdSendTrap_Object=MibTableColumn
rbnIpPoolContextThresholdSendTrap=_RbnIpPoolContextThresholdSendTrap_Object((1,3,6,1,4,1,2352,2,15,1,2,7,1,3),_RbnIpPoolContextThresholdSendTrap_Type())
rbnIpPoolContextThresholdSendTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextThresholdSendTrap.setStatus(_B)
_RbnIpPoolContextThresholdLogMessage_Type=TruthValue
_RbnIpPoolContextThresholdLogMessage_Object=MibTableColumn
rbnIpPoolContextThresholdLogMessage=_RbnIpPoolContextThresholdLogMessage_Object((1,3,6,1,4,1,2352,2,15,1,2,7,1,4),_RbnIpPoolContextThresholdLogMessage_Type())
rbnIpPoolContextThresholdLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpPoolContextThresholdLogMessage.setStatus(_B)
_RbnInetIpPoolTable_Object=MibTable
rbnInetIpPoolTable=_RbnInetIpPoolTable_Object((1,3,6,1,4,1,2352,2,15,1,3))
if mibBuilder.loadTexts:rbnInetIpPoolTable.setStatus(_B)
_RbnInetIpPoolEntry_Object=MibTableRow
rbnInetIpPoolEntry=_RbnInetIpPoolEntry_Object((1,3,6,1,4,1,2352,2,15,1,3,1))
rbnInetIpPoolEntry.setIndexNames((0,_A,_A0),(0,_A,_A1),(0,_A,_A2),(0,_A,_A3),(0,_A,_A4))
if mibBuilder.loadTexts:rbnInetIpPoolEntry.setStatus(_B)
_RbnInetIpPoolType_Type=RbnInetPoolType
_RbnInetIpPoolType_Object=MibTableColumn
rbnInetIpPoolType=_RbnInetIpPoolType_Object((1,3,6,1,4,1,2352,2,15,1,3,1,1),_RbnInetIpPoolType_Type())
rbnInetIpPoolType.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnInetIpPoolType.setStatus(_B)
_RbnInetIpPoolIfIndex_Type=InterfaceIndex
_RbnInetIpPoolIfIndex_Object=MibTableColumn
rbnInetIpPoolIfIndex=_RbnInetIpPoolIfIndex_Object((1,3,6,1,4,1,2352,2,15,1,3,1,2),_RbnInetIpPoolIfIndex_Type())
rbnInetIpPoolIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnInetIpPoolIfIndex.setStatus(_B)
_RbnInetIpPoolStartPrefixType_Type=InetAddressType
_RbnInetIpPoolStartPrefixType_Object=MibTableColumn
rbnInetIpPoolStartPrefixType=_RbnInetIpPoolStartPrefixType_Object((1,3,6,1,4,1,2352,2,15,1,3,1,3),_RbnInetIpPoolStartPrefixType_Type())
rbnInetIpPoolStartPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnInetIpPoolStartPrefixType.setStatus(_B)
_RbnInetIpPoolStartPrefix_Type=InetAddress
_RbnInetIpPoolStartPrefix_Object=MibTableColumn
rbnInetIpPoolStartPrefix=_RbnInetIpPoolStartPrefix_Object((1,3,6,1,4,1,2352,2,15,1,3,1,4),_RbnInetIpPoolStartPrefix_Type())
rbnInetIpPoolStartPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnInetIpPoolStartPrefix.setStatus(_B)
class _RbnInetIpPoolStartPrefixLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RbnInetIpPoolStartPrefixLen_Type.__name__=_h
_RbnInetIpPoolStartPrefixLen_Object=MibTableColumn
rbnInetIpPoolStartPrefixLen=_RbnInetIpPoolStartPrefixLen_Object((1,3,6,1,4,1,2352,2,15,1,3,1,5),_RbnInetIpPoolStartPrefixLen_Type())
rbnInetIpPoolStartPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnInetIpPoolStartPrefixLen.setStatus(_B)
_RbnInetIpPoolEndPrefixType_Type=InetAddressType
_RbnInetIpPoolEndPrefixType_Object=MibTableColumn
rbnInetIpPoolEndPrefixType=_RbnInetIpPoolEndPrefixType_Object((1,3,6,1,4,1,2352,2,15,1,3,1,6),_RbnInetIpPoolEndPrefixType_Type())
rbnInetIpPoolEndPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolEndPrefixType.setStatus(_B)
_RbnInetIpPoolEndPrefix_Type=InetAddress
_RbnInetIpPoolEndPrefix_Object=MibTableColumn
rbnInetIpPoolEndPrefix=_RbnInetIpPoolEndPrefix_Object((1,3,6,1,4,1,2352,2,15,1,3,1,7),_RbnInetIpPoolEndPrefix_Type())
rbnInetIpPoolEndPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolEndPrefix.setStatus(_B)
class _RbnInetIpPoolEndPrefixLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RbnInetIpPoolEndPrefixLen_Type.__name__=_h
_RbnInetIpPoolEndPrefixLen_Object=MibTableColumn
rbnInetIpPoolEndPrefixLen=_RbnInetIpPoolEndPrefixLen_Object((1,3,6,1,4,1,2352,2,15,1,3,1,8),_RbnInetIpPoolEndPrefixLen_Type())
rbnInetIpPoolEndPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolEndPrefixLen.setStatus(_B)
_RbnInetIpPoolInterfaceName_Type=SnmpAdminString
_RbnInetIpPoolInterfaceName_Object=MibTableColumn
rbnInetIpPoolInterfaceName=_RbnInetIpPoolInterfaceName_Object((1,3,6,1,4,1,2352,2,15,1,3,1,9),_RbnInetIpPoolInterfaceName_Type())
rbnInetIpPoolInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolInterfaceName.setStatus(_B)
_RbnInetIpPoolName_Type=SnmpAdminString
_RbnInetIpPoolName_Object=MibTableColumn
rbnInetIpPoolName=_RbnInetIpPoolName_Object((1,3,6,1,4,1,2352,2,15,1,3,1,10),_RbnInetIpPoolName_Type())
rbnInetIpPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolName.setStatus(_B)
_RbnInetIpPoolSize_Type=Unsigned32
_RbnInetIpPoolSize_Object=MibTableColumn
rbnInetIpPoolSize=_RbnInetIpPoolSize_Object((1,3,6,1,4,1,2352,2,15,1,3,1,11),_RbnInetIpPoolSize_Type())
rbnInetIpPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolSize.setStatus(_B)
_RbnInetIpPoolAvailable_Type=Unsigned32
_RbnInetIpPoolAvailable_Object=MibTableColumn
rbnInetIpPoolAvailable=_RbnInetIpPoolAvailable_Object((1,3,6,1,4,1,2352,2,15,1,3,1,12),_RbnInetIpPoolAvailable_Type())
rbnInetIpPoolAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolAvailable.setStatus(_B)
_RbnInetIpPoolUnusable_Type=Unsigned32
_RbnInetIpPoolUnusable_Object=MibTableColumn
rbnInetIpPoolUnusable=_RbnInetIpPoolUnusable_Object((1,3,6,1,4,1,2352,2,15,1,3,1,13),_RbnInetIpPoolUnusable_Type())
rbnInetIpPoolUnusable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolUnusable.setStatus(_B)
_RbnInetIpPoolInuse_Type=Unsigned32
_RbnInetIpPoolInuse_Object=MibTableColumn
rbnInetIpPoolInuse=_RbnInetIpPoolInuse_Object((1,3,6,1,4,1,2352,2,15,1,3,1,14),_RbnInetIpPoolInuse_Type())
rbnInetIpPoolInuse.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolInuse.setStatus(_B)
_RbnInetIpPoolThrshType_Type=RbnInetIpPoolThresholdType
_RbnInetIpPoolThrshType_Object=MibTableColumn
rbnInetIpPoolThrshType=_RbnInetIpPoolThrshType_Object((1,3,6,1,4,1,2352,2,15,1,3,1,15),_RbnInetIpPoolThrshType_Type())
rbnInetIpPoolThrshType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolThrshType.setStatus(_B)
_RbnInetIpPoolHiFallingThrsh_Type=RbnInetIpPoolThreshold
_RbnInetIpPoolHiFallingThrsh_Object=MibTableColumn
rbnInetIpPoolHiFallingThrsh=_RbnInetIpPoolHiFallingThrsh_Object((1,3,6,1,4,1,2352,2,15,1,3,1,16),_RbnInetIpPoolHiFallingThrsh_Type())
rbnInetIpPoolHiFallingThrsh.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolHiFallingThrsh.setStatus(_B)
_RbnInetIpPoolHiFallingNotify_Type=RbnInetIpPoolThrshNotify
_RbnInetIpPoolHiFallingNotify_Object=MibTableColumn
rbnInetIpPoolHiFallingNotify=_RbnInetIpPoolHiFallingNotify_Object((1,3,6,1,4,1,2352,2,15,1,3,1,17),_RbnInetIpPoolHiFallingNotify_Type())
rbnInetIpPoolHiFallingNotify.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolHiFallingNotify.setStatus(_B)
_RbnInetIpPoolLoFallingThrsh_Type=RbnInetIpPoolThreshold
_RbnInetIpPoolLoFallingThrsh_Object=MibTableColumn
rbnInetIpPoolLoFallingThrsh=_RbnInetIpPoolLoFallingThrsh_Object((1,3,6,1,4,1,2352,2,15,1,3,1,18),_RbnInetIpPoolLoFallingThrsh_Type())
rbnInetIpPoolLoFallingThrsh.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolLoFallingThrsh.setStatus(_B)
_RbnInetIpPoolLoFallingNotify_Type=RbnInetIpPoolThrshNotify
_RbnInetIpPoolLoFallingNotify_Object=MibTableColumn
rbnInetIpPoolLoFallingNotify=_RbnInetIpPoolLoFallingNotify_Object((1,3,6,1,4,1,2352,2,15,1,3,1,19),_RbnInetIpPoolLoFallingNotify_Type())
rbnInetIpPoolLoFallingNotify.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolLoFallingNotify.setStatus(_B)
_RbnInetIpPoolSummary_ObjectIdentity=ObjectIdentity
rbnInetIpPoolSummary=_RbnInetIpPoolSummary_ObjectIdentity((1,3,6,1,4,1,2352,2,15,1,4))
_RbnInetIpPoolCtxName_Type=SnmpAdminString
_RbnInetIpPoolCtxName_Object=MibScalar
rbnInetIpPoolCtxName=_RbnInetIpPoolCtxName_Object((1,3,6,1,4,1,2352,2,15,1,4,1),_RbnInetIpPoolCtxName_Type())
rbnInetIpPoolCtxName.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:rbnInetIpPoolCtxName.setStatus(_B)
_RbnInetIpPoolCtxTable_Object=MibTable
rbnInetIpPoolCtxTable=_RbnInetIpPoolCtxTable_Object((1,3,6,1,4,1,2352,2,15,1,4,2))
if mibBuilder.loadTexts:rbnInetIpPoolCtxTable.setStatus(_B)
_RbnInetIpPoolCtxEntry_Object=MibTableRow
rbnInetIpPoolCtxEntry=_RbnInetIpPoolCtxEntry_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1))
rbnInetIpPoolCtxEntry.setIndexNames((0,_A,_A5))
if mibBuilder.loadTexts:rbnInetIpPoolCtxEntry.setStatus(_B)
_RbnInetIpPoolCtxPoolType_Type=RbnInetPoolType
_RbnInetIpPoolCtxPoolType_Object=MibTableColumn
rbnInetIpPoolCtxPoolType=_RbnInetIpPoolCtxPoolType_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,1),_RbnInetIpPoolCtxPoolType_Type())
rbnInetIpPoolCtxPoolType.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnInetIpPoolCtxPoolType.setStatus(_B)
_RbnInetIpPoolCtxAvailable_Type=Unsigned32
_RbnInetIpPoolCtxAvailable_Object=MibTableColumn
rbnInetIpPoolCtxAvailable=_RbnInetIpPoolCtxAvailable_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,2),_RbnInetIpPoolCtxAvailable_Type())
rbnInetIpPoolCtxAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxAvailable.setStatus(_B)
_RbnInetIpPoolCtxPoolSize_Type=Unsigned32
_RbnInetIpPoolCtxPoolSize_Object=MibTableColumn
rbnInetIpPoolCtxPoolSize=_RbnInetIpPoolCtxPoolSize_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,3),_RbnInetIpPoolCtxPoolSize_Type())
rbnInetIpPoolCtxPoolSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxPoolSize.setStatus(_B)
_RbnInetIpPoolCtxThrshType_Type=RbnInetIpPoolThresholdType
_RbnInetIpPoolCtxThrshType_Object=MibTableColumn
rbnInetIpPoolCtxThrshType=_RbnInetIpPoolCtxThrshType_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,4),_RbnInetIpPoolCtxThrshType_Type())
rbnInetIpPoolCtxThrshType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxThrshType.setStatus(_B)
_RbnInetIpPoolCtxHiFallingThrsh_Type=RbnInetIpPoolThreshold
_RbnInetIpPoolCtxHiFallingThrsh_Object=MibTableColumn
rbnInetIpPoolCtxHiFallingThrsh=_RbnInetIpPoolCtxHiFallingThrsh_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,5),_RbnInetIpPoolCtxHiFallingThrsh_Type())
rbnInetIpPoolCtxHiFallingThrsh.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxHiFallingThrsh.setStatus(_B)
_RbnInetIpPoolCtxHiFallingNotify_Type=RbnInetIpPoolThrshNotify
_RbnInetIpPoolCtxHiFallingNotify_Object=MibTableColumn
rbnInetIpPoolCtxHiFallingNotify=_RbnInetIpPoolCtxHiFallingNotify_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,6),_RbnInetIpPoolCtxHiFallingNotify_Type())
rbnInetIpPoolCtxHiFallingNotify.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxHiFallingNotify.setStatus(_B)
_RbnInetIpPoolCtxLoFallingThrsh_Type=RbnInetIpPoolThreshold
_RbnInetIpPoolCtxLoFallingThrsh_Object=MibTableColumn
rbnInetIpPoolCtxLoFallingThrsh=_RbnInetIpPoolCtxLoFallingThrsh_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,7),_RbnInetIpPoolCtxLoFallingThrsh_Type())
rbnInetIpPoolCtxLoFallingThrsh.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxLoFallingThrsh.setStatus(_B)
_RbnInetIpPoolCtxLoFallingNotify_Type=RbnInetIpPoolThrshNotify
_RbnInetIpPoolCtxLoFallingNotify_Object=MibTableColumn
rbnInetIpPoolCtxLoFallingNotify=_RbnInetIpPoolCtxLoFallingNotify_Object((1,3,6,1,4,1,2352,2,15,1,4,2,1,8),_RbnInetIpPoolCtxLoFallingNotify_Type())
rbnInetIpPoolCtxLoFallingNotify.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnInetIpPoolCtxLoFallingNotify.setStatus(_B)
_RbnIpPoolMIBConformance_ObjectIdentity=ObjectIdentity
rbnIpPoolMIBConformance=_RbnIpPoolMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,15,2))
_RbnIpPoolCompliances_ObjectIdentity=ObjectIdentity
rbnIpPoolCompliances=_RbnIpPoolCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,15,2,1))
_RbnIpPoolGroups_ObjectIdentity=ObjectIdentity
rbnIpPoolGroups=_RbnIpPoolGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,15,2,2))
rbnIpPoolGroup=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,1))
rbnIpPoolGroup.setObjects(*((_A,_H),(_A,_I),(_A,_N),(_A,_J),(_A,_O),(_A,_P),(_A,_K),(_A,_Q),(_A,_R),(_A,_E),(_A,_F),(_A,_L),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:rbnIpPoolGroup.setStatus(_B)
rbnIpPoolNameGroup=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,3))
rbnIpPoolNameGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:rbnIpPoolNameGroup.setStatus(_B)
rbnIpPoolGroupV2=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,4))
rbnIpPoolGroupV2.setObjects(*((_A,_H),(_A,_I),(_A,_N),(_A,_J),(_A,_O),(_A,_P),(_A,_K),(_A,_Q),(_A,_R),(_A,_j),(_A,_E),(_A,_F),(_A,_L),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:rbnIpPoolGroupV2.setStatus(_B)
rbnIpPoolRangeGroup=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,5))
rbnIpPoolRangeGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:rbnIpPoolRangeGroup.setStatus(_B)
rbnIpPoolInterfaceGroup=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,6))
rbnIpPoolInterfaceGroup.setObjects(*((_A,_H),(_A,_I),(_A,_N),(_A,_J),(_A,_O),(_A,_P),(_A,_K),(_A,_Q),(_A,_R),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:rbnIpPoolInterfaceGroup.setStatus(_B)
rbnIpPoolContextGroup=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,7))
rbnIpPoolContextGroup.setObjects(*((_A,_E),(_A,_F),(_A,_L),(_A,_S),(_A,_T),(_A,_l),(_A,_m),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:rbnIpPoolContextGroup.setStatus(_B)
rbnInetIpPoolGroup=ObjectGroup((1,3,6,1,4,1,2352,2,15,2,2,9))
rbnInetIpPoolGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_A8),(_A,_A9),(_A,_b),(_A,_n),(_A,_AA),(_A,_o),(_A,_AB),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_p),(_A,_AC),(_A,_q),(_A,_AD)))
if mibBuilder.loadTexts:rbnInetIpPoolGroup.setStatus(_B)
rbnIpPoolThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,1))
rbnIpPoolThresholdMet.setObjects(*((_A,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnIpPoolThresholdMet.setStatus(_B)
rbnIpPoolContextThresholdMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,2))
rbnIpPoolContextThresholdMet.setObjects(*((_A,_E),(_A,_F),(_A,_L)))
if mibBuilder.loadTexts:rbnIpPoolContextThresholdMet.setStatus(_B)
rbnIpPoolContextThresholdPercentageMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,3))
rbnIpPoolContextThresholdPercentageMet.setObjects(*((_A,_E),(_A,_l),(_A,_F),(_A,_m)))
if mibBuilder.loadTexts:rbnIpPoolContextThresholdPercentageMet.setStatus(_B)
rbnInetIpPoolHiFallingThrshMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,4))
rbnInetIpPoolHiFallingThrshMet.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_n)))
if mibBuilder.loadTexts:rbnInetIpPoolHiFallingThrshMet.setStatus(_B)
rbnInetIpPoolLoFallingThrshMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,5))
rbnInetIpPoolLoFallingThrshMet.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_o)))
if mibBuilder.loadTexts:rbnInetIpPoolLoFallingThrshMet.setStatus(_B)
rbnInetIpPoolCtxHiFallingThrshMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,6))
rbnInetIpPoolCtxHiFallingThrshMet.setObjects(*((_A,_c),(_A,_e),(_A,_d),(_A,_f),(_A,_p)))
if mibBuilder.loadTexts:rbnInetIpPoolCtxHiFallingThrshMet.setStatus(_B)
rbnInetIpPoolCtxLoFallingThrshMet=NotificationType((1,3,6,1,4,1,2352,2,15,0,7))
rbnInetIpPoolCtxLoFallingThrshMet.setObjects(*((_A,_c),(_A,_e),(_A,_d),(_A,_f),(_A,_q)))
if mibBuilder.loadTexts:rbnInetIpPoolCtxLoFallingThrshMet.setStatus(_B)
rbnIpPoolNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,15,2,2,2))
rbnIpPoolNotifyGroup.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:rbnIpPoolNotifyGroup.setStatus(_B)
rbnIpPoolNotifyGroupV2=NotificationGroup((1,3,6,1,4,1,2352,2,15,2,2,8))
rbnIpPoolNotifyGroupV2.setObjects(*((_A,_r),(_A,_s),(_A,_AE)))
if mibBuilder.loadTexts:rbnIpPoolNotifyGroupV2.setStatus(_B)
rbnInetIpPoolNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,15,2,2,10))
rbnInetIpPoolNotifyGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:rbnInetIpPoolNotifyGroup.setStatus(_B)
rbnIpPoolCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,1))
rbnIpPoolCompliance.setObjects(*((_A,_t),(_A,_G)))
if mibBuilder.loadTexts:rbnIpPoolCompliance.setStatus(_B)
rbnIpPoolNameCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,2))
rbnIpPoolNameCompliance.setObjects(*((_A,_t),(_A,_G),(_A,_u)))
if mibBuilder.loadTexts:rbnIpPoolNameCompliance.setStatus(_B)
rbnIpPoolComplianceV2=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,3))
rbnIpPoolComplianceV2.setObjects(*((_A,_g),(_A,_G)))
if mibBuilder.loadTexts:rbnIpPoolComplianceV2.setStatus(_B)
rbnIpPoolNameComplianceV2=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,4))
rbnIpPoolNameComplianceV2.setObjects(*((_A,_g),(_A,_G),(_A,_u)))
if mibBuilder.loadTexts:rbnIpPoolNameComplianceV2.setStatus(_B)
rbnIpPoolRangeCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,5))
rbnIpPoolRangeCompliance.setObjects(*((_A,_g),(_A,_G),(_A,_AJ)))
if mibBuilder.loadTexts:rbnIpPoolRangeCompliance.setStatus(_B)
rbnIpPoolThresholdPercentCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,6))
rbnIpPoolThresholdPercentCompliance.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:rbnIpPoolThresholdPercentCompliance.setStatus(_B)
rbnInetIpPoolCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,15,2,1,7))
rbnInetIpPoolCompliance.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:rbnInetIpPoolCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RbnInetPoolType':RbnInetPoolType,'RbnInetIpPoolThresholdType':RbnInetIpPoolThresholdType,'RbnInetIpPoolThreshold':RbnInetIpPoolThreshold,'RbnInetIpPoolThrshNotify':RbnInetIpPoolThrshNotify,'rbnIpPoolMib':rbnIpPoolMib,'rbnIpPoolMIBNotifications':rbnIpPoolMIBNotifications,_r:rbnIpPoolThresholdMet,_s:rbnIpPoolContextThresholdMet,_AE:rbnIpPoolContextThresholdPercentageMet,_AF:rbnInetIpPoolHiFallingThrshMet,_AG:rbnInetIpPoolLoFallingThrshMet,_AH:rbnInetIpPoolCtxHiFallingThrshMet,_AI:rbnInetIpPoolCtxLoFallingThrshMet,'rbnIpPoolMIBObjects':rbnIpPoolMIBObjects,'rbnIpPoolTable':rbnIpPoolTable,'rbnIpPoolEntry':rbnIpPoolEntry,_x:rbnIpPoolInterfaceIdx,_y:rbnIpPoolAddr,_H:rbnIpPoolInterfaceName,_I:rbnIpPoolMask,_N:rbnIpPoolSize,_J:rbnIpPoolAvailable,_O:rbnIpPoolUnusable,_P:rbnIpPoolInuse,_K:rbnIpPoolThreshold,_Q:rbnIpPoolSendTrap,_R:rbnIpPoolLogMessage,_i:rbnIpPoolName,_j:rbnIpPoolType,_k:rbnIpPoolEndAddr,'rbnIpPoolSummary':rbnIpPoolSummary,_E:rbnIpPoolContextName,_F:rbnIpPoolContextAvailable,_L:rbnIpPoolContextThreshold,_S:rbnIpPoolContextSendTrap,_T:rbnIpPoolContextLogMessage,_l:rbnIpPoolContextTotalSize,'rbnIpPoolContextThresholdPercentTable':rbnIpPoolContextThresholdPercentTable,'rbnIpPoolContextThresholdPercentEntry':rbnIpPoolContextThresholdPercentEntry,_z:rbnIpPoolContextThresholdIndex,_m:rbnIpPoolContextThresholdPercentage,_A6:rbnIpPoolContextThresholdSendTrap,_A7:rbnIpPoolContextThresholdLogMessage,'rbnInetIpPoolTable':rbnInetIpPoolTable,'rbnInetIpPoolEntry':rbnInetIpPoolEntry,_A0:rbnInetIpPoolType,_A1:rbnInetIpPoolIfIndex,_A2:rbnInetIpPoolStartPrefixType,_A3:rbnInetIpPoolStartPrefix,_A4:rbnInetIpPoolStartPrefixLen,_U:rbnInetIpPoolEndPrefixType,_V:rbnInetIpPoolEndPrefix,_W:rbnInetIpPoolEndPrefixLen,_X:rbnInetIpPoolInterfaceName,_Y:rbnInetIpPoolName,_Z:rbnInetIpPoolSize,_a:rbnInetIpPoolAvailable,_A8:rbnInetIpPoolUnusable,_A9:rbnInetIpPoolInuse,_b:rbnInetIpPoolThrshType,_n:rbnInetIpPoolHiFallingThrsh,_AA:rbnInetIpPoolHiFallingNotify,_o:rbnInetIpPoolLoFallingThrsh,_AB:rbnInetIpPoolLoFallingNotify,'rbnInetIpPoolSummary':rbnInetIpPoolSummary,_c:rbnInetIpPoolCtxName,'rbnInetIpPoolCtxTable':rbnInetIpPoolCtxTable,'rbnInetIpPoolCtxEntry':rbnInetIpPoolCtxEntry,_A5:rbnInetIpPoolCtxPoolType,_d:rbnInetIpPoolCtxAvailable,_e:rbnInetIpPoolCtxPoolSize,_f:rbnInetIpPoolCtxThrshType,_p:rbnInetIpPoolCtxHiFallingThrsh,_AC:rbnInetIpPoolCtxHiFallingNotify,_q:rbnInetIpPoolCtxLoFallingThrsh,_AD:rbnInetIpPoolCtxLoFallingNotify,'rbnIpPoolMIBConformance':rbnIpPoolMIBConformance,'rbnIpPoolCompliances':rbnIpPoolCompliances,'rbnIpPoolCompliance':rbnIpPoolCompliance,'rbnIpPoolNameCompliance':rbnIpPoolNameCompliance,'rbnIpPoolComplianceV2':rbnIpPoolComplianceV2,'rbnIpPoolNameComplianceV2':rbnIpPoolNameComplianceV2,'rbnIpPoolRangeCompliance':rbnIpPoolRangeCompliance,'rbnIpPoolThresholdPercentCompliance':rbnIpPoolThresholdPercentCompliance,'rbnInetIpPoolCompliance':rbnInetIpPoolCompliance,'rbnIpPoolGroups':rbnIpPoolGroups,_t:rbnIpPoolGroup,_G:rbnIpPoolNotifyGroup,_u:rbnIpPoolNameGroup,_g:rbnIpPoolGroupV2,_AJ:rbnIpPoolRangeGroup,_AK:rbnIpPoolInterfaceGroup,_AL:rbnIpPoolContextGroup,_AM:rbnIpPoolNotifyGroupV2,_AN:rbnInetIpPoolGroup,_AO:rbnInetIpPoolNotifyGroup})