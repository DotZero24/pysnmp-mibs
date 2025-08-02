_J='mitelPppOEthTableIndex'
_I='read-create'
_H='mitelRmtCfgTableIndex'
_G='override'
_F='accept'
_E='MITEL-PPPGROUP-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelRouterPppGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,2))
if mibBuilder.loadTexts:mitelRouterPppGroup.setRevisions(('2003-03-24 10:33','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelPppGrpGlobalGroup_ObjectIdentity=ObjectIdentity
mitelPppGrpGlobalGroup=_MitelPppGrpGlobalGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,2,1))
class _MitelGblGrpNegotiateFirst_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chap',1),('pap',2),('mschap',3)))
_MitelGblGrpNegotiateFirst_Type.__name__=_C
_MitelGblGrpNegotiateFirst_Object=MibScalar
mitelGblGrpNegotiateFirst=_MitelGblGrpNegotiateFirst_Object((1,3,6,1,4,1,1027,4,8,1,2,1,1),_MitelGblGrpNegotiateFirst_Type())
mitelGblGrpNegotiateFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpNegotiateFirst.setStatus(_A)
_MitelGblGrpDynamicIpAddr_Type=IpAddress
_MitelGblGrpDynamicIpAddr_Object=MibScalar
mitelGblGrpDynamicIpAddr=_MitelGblGrpDynamicIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,2,1,2),_MitelGblGrpDynamicIpAddr_Type())
mitelGblGrpDynamicIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpDynamicIpAddr.setStatus(_A)
class _MitelGblGrpNumDynamicIpAddr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_MitelGblGrpNumDynamicIpAddr_Type.__name__=_C
_MitelGblGrpNumDynamicIpAddr_Object=MibScalar
mitelGblGrpNumDynamicIpAddr=_MitelGblGrpNumDynamicIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,2,1,3),_MitelGblGrpNumDynamicIpAddr_Type())
mitelGblGrpNumDynamicIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpNumDynamicIpAddr.setStatus(_A)
class _MitelGblGrpDynamicIpAdrrHoldoff_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_MitelGblGrpDynamicIpAdrrHoldoff_Type.__name__=_C
_MitelGblGrpDynamicIpAdrrHoldoff_Object=MibScalar
mitelGblGrpDynamicIpAdrrHoldoff=_MitelGblGrpDynamicIpAdrrHoldoff_Object((1,3,6,1,4,1,1027,4,8,1,2,1,4),_MitelGblGrpDynamicIpAdrrHoldoff_Type())
mitelGblGrpDynamicIpAdrrHoldoff.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpDynamicIpAdrrHoldoff.setStatus(_A)
class _MitelGblGrpRemDnsIpAddrHandling_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),('overridewith',3)))
_MitelGblGrpRemDnsIpAddrHandling_Type.__name__=_C
_MitelGblGrpRemDnsIpAddrHandling_Object=MibScalar
mitelGblGrpRemDnsIpAddrHandling=_MitelGblGrpRemDnsIpAddrHandling_Object((1,3,6,1,4,1,1027,4,8,1,2,1,5),_MitelGblGrpRemDnsIpAddrHandling_Type())
mitelGblGrpRemDnsIpAddrHandling.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpRemDnsIpAddrHandling.setStatus(_A)
_MitelGblGrpPrimaryWinsServerIpAddr_Type=IpAddress
_MitelGblGrpPrimaryWinsServerIpAddr_Object=MibScalar
mitelGblGrpPrimaryWinsServerIpAddr=_MitelGblGrpPrimaryWinsServerIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,2,1,6),_MitelGblGrpPrimaryWinsServerIpAddr_Type())
mitelGblGrpPrimaryWinsServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpPrimaryWinsServerIpAddr.setStatus(_A)
_MitelGblGrpSecondaryWinsServerIpAddr_Type=IpAddress
_MitelGblGrpSecondaryWinsServerIpAddr_Object=MibScalar
mitelGblGrpSecondaryWinsServerIpAddr=_MitelGblGrpSecondaryWinsServerIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,2,1,7),_MitelGblGrpSecondaryWinsServerIpAddr_Type())
mitelGblGrpSecondaryWinsServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelGblGrpSecondaryWinsServerIpAddr.setStatus(_A)
_MitelPppGrpRemoteConfigTable_Object=MibTable
mitelPppGrpRemoteConfigTable=_MitelPppGrpRemoteConfigTable_Object((1,3,6,1,4,1,1027,4,8,1,2,2))
if mibBuilder.loadTexts:mitelPppGrpRemoteConfigTable.setStatus(_A)
_MitelPppGrpRemoteConfigEntry_Object=MibTableRow
mitelPppGrpRemoteConfigEntry=_MitelPppGrpRemoteConfigEntry_Object((1,3,6,1,4,1,1027,4,8,1,2,2,1))
mitelPppGrpRemoteConfigEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:mitelPppGrpRemoteConfigEntry.setStatus(_A)
_MitelRmtCfgTableIndex_Type=Integer32
_MitelRmtCfgTableIndex_Object=MibTableColumn
mitelRmtCfgTableIndex=_MitelRmtCfgTableIndex_Object((1,3,6,1,4,1,1027,4,8,1,2,2,1,1),_MitelRmtCfgTableIndex_Type())
mitelRmtCfgTableIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:mitelRmtCfgTableIndex.setStatus(_A)
class _MitelRmtCfgTableIpAddrHandling_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),('assign',3)))
_MitelRmtCfgTableIpAddrHandling_Type.__name__=_C
_MitelRmtCfgTableIpAddrHandling_Object=MibTableColumn
mitelRmtCfgTableIpAddrHandling=_MitelRmtCfgTableIpAddrHandling_Object((1,3,6,1,4,1,1027,4,8,1,2,2,1,2),_MitelRmtCfgTableIpAddrHandling_Type())
mitelRmtCfgTableIpAddrHandling.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelRmtCfgTableIpAddrHandling.setStatus(_A)
_MitelRmtCfgTableRemIpAddr_Type=IpAddress
_MitelRmtCfgTableRemIpAddr_Object=MibTableColumn
mitelRmtCfgTableRemIpAddr=_MitelRmtCfgTableRemIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,2,2,1,3),_MitelRmtCfgTableRemIpAddr_Type())
mitelRmtCfgTableRemIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelRmtCfgTableRemIpAddr.setStatus(_A)
_MitelRmtCfgTableStatus_Type=RowStatus
_MitelRmtCfgTableStatus_Object=MibTableColumn
mitelRmtCfgTableStatus=_MitelRmtCfgTableStatus_Object((1,3,6,1,4,1,1027,4,8,1,2,2,1,4),_MitelRmtCfgTableStatus_Type())
mitelRmtCfgTableStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:mitelRmtCfgTableStatus.setStatus(_A)
class _MitelRmtCfgTablePppMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('client',1),('server',2)))
_MitelRmtCfgTablePppMode_Type.__name__=_C
_MitelRmtCfgTablePppMode_Object=MibTableColumn
mitelRmtCfgTablePppMode=_MitelRmtCfgTablePppMode_Object((1,3,6,1,4,1,1027,4,8,1,2,2,1,5),_MitelRmtCfgTablePppMode_Type())
mitelRmtCfgTablePppMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelRmtCfgTablePppMode.setStatus(_A)
_MitelPppGrpPppOverEthernetTable_Object=MibTable
mitelPppGrpPppOverEthernetTable=_MitelPppGrpPppOverEthernetTable_Object((1,3,6,1,4,1,1027,4,8,1,2,3))
if mibBuilder.loadTexts:mitelPppGrpPppOverEthernetTable.setStatus(_A)
_MitelPppGrpPppOverEthernetEntry_Object=MibTableRow
mitelPppGrpPppOverEthernetEntry=_MitelPppGrpPppOverEthernetEntry_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1))
mitelPppGrpPppOverEthernetEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:mitelPppGrpPppOverEthernetEntry.setStatus(_A)
_MitelPppOEthTableIndex_Type=Integer32
_MitelPppOEthTableIndex_Object=MibTableColumn
mitelPppOEthTableIndex=_MitelPppOEthTableIndex_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,1),_MitelPppOEthTableIndex_Type())
mitelPppOEthTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTableIndex.setStatus(_A)
class _MitelPppOEthTableEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_MitelPppOEthTableEnabled_Type.__name__=_C
_MitelPppOEthTableEnabled_Object=MibTableColumn
mitelPppOEthTableEnabled=_MitelPppOEthTableEnabled_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,2),_MitelPppOEthTableEnabled_Type())
mitelPppOEthTableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTableEnabled.setStatus(_A)
class _MitelPppOEthTablePacketTimeout_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_MitelPppOEthTablePacketTimeout_Type.__name__=_C
_MitelPppOEthTablePacketTimeout_Object=MibTableColumn
mitelPppOEthTablePacketTimeout=_MitelPppOEthTablePacketTimeout_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,3),_MitelPppOEthTablePacketTimeout_Type())
mitelPppOEthTablePacketTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTablePacketTimeout.setStatus(_A)
class _MitelPppOEthTablePacketRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_MitelPppOEthTablePacketRetries_Type.__name__=_C
_MitelPppOEthTablePacketRetries_Object=MibTableColumn
mitelPppOEthTablePacketRetries=_MitelPppOEthTablePacketRetries_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,4),_MitelPppOEthTablePacketRetries_Type())
mitelPppOEthTablePacketRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTablePacketRetries.setStatus(_A)
class _MitelPppOEthTableTotalRetries_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_MitelPppOEthTableTotalRetries_Type.__name__=_C
_MitelPppOEthTableTotalRetries_Object=MibTableColumn
mitelPppOEthTableTotalRetries=_MitelPppOEthTableTotalRetries_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,5),_MitelPppOEthTableTotalRetries_Type())
mitelPppOEthTableTotalRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTableTotalRetries.setStatus(_A)
class _MitelPppOEthTableServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_MitelPppOEthTableServiceName_Type.__name__=_D
_MitelPppOEthTableServiceName_Object=MibTableColumn
mitelPppOEthTableServiceName=_MitelPppOEthTableServiceName_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,6),_MitelPppOEthTableServiceName_Type())
mitelPppOEthTableServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTableServiceName.setStatus(_A)
class _MitelPppOEthTableACName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_MitelPppOEthTableACName_Type.__name__=_D
_MitelPppOEthTableACName_Object=MibTableColumn
mitelPppOEthTableACName=_MitelPppOEthTableACName_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,7),_MitelPppOEthTableACName_Type())
mitelPppOEthTableACName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelPppOEthTableACName.setStatus(_A)
_MitelPppOEthTableStatus_Type=RowStatus
_MitelPppOEthTableStatus_Object=MibTableColumn
mitelPppOEthTableStatus=_MitelPppOEthTableStatus_Object((1,3,6,1,4,1,1027,4,8,1,2,3,1,8),_MitelPppOEthTableStatus_Type())
mitelPppOEthTableStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:mitelPppOEthTableStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterPppGroup':mitelRouterPppGroup,'mitelPppGrpGlobalGroup':mitelPppGrpGlobalGroup,'mitelGblGrpNegotiateFirst':mitelGblGrpNegotiateFirst,'mitelGblGrpDynamicIpAddr':mitelGblGrpDynamicIpAddr,'mitelGblGrpNumDynamicIpAddr':mitelGblGrpNumDynamicIpAddr,'mitelGblGrpDynamicIpAdrrHoldoff':mitelGblGrpDynamicIpAdrrHoldoff,'mitelGblGrpRemDnsIpAddrHandling':mitelGblGrpRemDnsIpAddrHandling,'mitelGblGrpPrimaryWinsServerIpAddr':mitelGblGrpPrimaryWinsServerIpAddr,'mitelGblGrpSecondaryWinsServerIpAddr':mitelGblGrpSecondaryWinsServerIpAddr,'mitelPppGrpRemoteConfigTable':mitelPppGrpRemoteConfigTable,'mitelPppGrpRemoteConfigEntry':mitelPppGrpRemoteConfigEntry,_H:mitelRmtCfgTableIndex,'mitelRmtCfgTableIpAddrHandling':mitelRmtCfgTableIpAddrHandling,'mitelRmtCfgTableRemIpAddr':mitelRmtCfgTableRemIpAddr,'mitelRmtCfgTableStatus':mitelRmtCfgTableStatus,'mitelRmtCfgTablePppMode':mitelRmtCfgTablePppMode,'mitelPppGrpPppOverEthernetTable':mitelPppGrpPppOverEthernetTable,'mitelPppGrpPppOverEthernetEntry':mitelPppGrpPppOverEthernetEntry,_J:mitelPppOEthTableIndex,'mitelPppOEthTableEnabled':mitelPppOEthTableEnabled,'mitelPppOEthTablePacketTimeout':mitelPppOEthTablePacketTimeout,'mitelPppOEthTablePacketRetries':mitelPppOEthTablePacketRetries,'mitelPppOEthTableTotalRetries':mitelPppOEthTableTotalRetries,'mitelPppOEthTableServiceName':mitelPppOEthTableServiceName,'mitelPppOEthTableACName':mitelPppOEthTableACName,'mitelPppOEthTableStatus':mitelPppOEthTableStatus})