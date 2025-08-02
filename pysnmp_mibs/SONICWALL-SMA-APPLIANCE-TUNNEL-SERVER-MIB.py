_E='tunnelServiceSslTunnelId'
_D='tunnelServiceClientAddrPoolId'
_C='SONICWALL-SMA-APPLIANCE-TUNNEL-SERVER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InternationalDisplayString,=mibBuilder.importSymbols('HOST-RESOURCES-MIB','InternationalDisplayString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sonicwallSMAAppliance,=mibBuilder.importSymbols('SONICWALL-SMA-MIB','sonicwallSMAAppliance')
sonicwallTunnelServer=ModuleIdentity((1,3,6,1,4,1,8741,8,1,5))
_TunnelServerState_Type=InternationalDisplayString
_TunnelServerState_Object=MibScalar
tunnelServerState=_TunnelServerState_Object((1,3,6,1,4,1,8741,8,1,5,1),_TunnelServerState_Type())
tunnelServerState.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServerState.setStatus(_A)
_NumOfTunnelServiceClientAddrPool_Type=Integer32
_NumOfTunnelServiceClientAddrPool_Object=MibScalar
numOfTunnelServiceClientAddrPool=_NumOfTunnelServiceClientAddrPool_Object((1,3,6,1,4,1,8741,8,1,5,2),_NumOfTunnelServiceClientAddrPool_Type())
numOfTunnelServiceClientAddrPool.setMaxAccess(_B)
if mibBuilder.loadTexts:numOfTunnelServiceClientAddrPool.setStatus(_A)
_TunnelServiceClientAddrPoolRangesTable_Object=MibTable
tunnelServiceClientAddrPoolRangesTable=_TunnelServiceClientAddrPoolRangesTable_Object((1,3,6,1,4,1,8741,8,1,5,3))
if mibBuilder.loadTexts:tunnelServiceClientAddrPoolRangesTable.setStatus(_A)
_TunnelServiceClientAddrPoolEntry_Object=MibTableRow
tunnelServiceClientAddrPoolEntry=_TunnelServiceClientAddrPoolEntry_Object((1,3,6,1,4,1,8741,8,1,5,3,1))
tunnelServiceClientAddrPoolEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:tunnelServiceClientAddrPoolEntry.setStatus(_A)
_TunnelServiceClientAddrPoolId_Type=Integer32
_TunnelServiceClientAddrPoolId_Object=MibTableColumn
tunnelServiceClientAddrPoolId=_TunnelServiceClientAddrPoolId_Object((1,3,6,1,4,1,8741,8,1,5,3,1,1),_TunnelServiceClientAddrPoolId_Type())
tunnelServiceClientAddrPoolId.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceClientAddrPoolId.setStatus(_A)
_TunnelServiceClientAddrPoolUtilization_Type=Integer32
_TunnelServiceClientAddrPoolUtilization_Object=MibTableColumn
tunnelServiceClientAddrPoolUtilization=_TunnelServiceClientAddrPoolUtilization_Object((1,3,6,1,4,1,8741,8,1,5,3,1,2),_TunnelServiceClientAddrPoolUtilization_Type())
tunnelServiceClientAddrPoolUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceClientAddrPoolUtilization.setStatus(_A)
_TunnelServiceStartRangeOfClientAddrPool_Type=InternationalDisplayString
_TunnelServiceStartRangeOfClientAddrPool_Object=MibTableColumn
tunnelServiceStartRangeOfClientAddrPool=_TunnelServiceStartRangeOfClientAddrPool_Object((1,3,6,1,4,1,8741,8,1,5,3,1,3),_TunnelServiceStartRangeOfClientAddrPool_Type())
tunnelServiceStartRangeOfClientAddrPool.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceStartRangeOfClientAddrPool.setStatus(_A)
_TunnelServiceEndRangeOfClientAddrPool_Type=InternationalDisplayString
_TunnelServiceEndRangeOfClientAddrPool_Object=MibTableColumn
tunnelServiceEndRangeOfClientAddrPool=_TunnelServiceEndRangeOfClientAddrPool_Object((1,3,6,1,4,1,8741,8,1,5,3,1,4),_TunnelServiceEndRangeOfClientAddrPool_Type())
tunnelServiceEndRangeOfClientAddrPool.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceEndRangeOfClientAddrPool.setStatus(_A)
_NumberOfTunnelServiceSslTunnels_Type=Integer32
_NumberOfTunnelServiceSslTunnels_Object=MibScalar
numberOfTunnelServiceSslTunnels=_NumberOfTunnelServiceSslTunnels_Object((1,3,6,1,4,1,8741,8,1,5,4),_NumberOfTunnelServiceSslTunnels_Type())
numberOfTunnelServiceSslTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:numberOfTunnelServiceSslTunnels.setStatus(_A)
_TunnelServiceSslTunnelTable_Object=MibTable
tunnelServiceSslTunnelTable=_TunnelServiceSslTunnelTable_Object((1,3,6,1,4,1,8741,8,1,5,5))
if mibBuilder.loadTexts:tunnelServiceSslTunnelTable.setStatus(_A)
_TunnelServiceSslTunnelEntry_Object=MibTableRow
tunnelServiceSslTunnelEntry=_TunnelServiceSslTunnelEntry_Object((1,3,6,1,4,1,8741,8,1,5,5,1))
tunnelServiceSslTunnelEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:tunnelServiceSslTunnelEntry.setStatus(_A)
_TunnelServiceSslTunnelId_Type=Integer32
_TunnelServiceSslTunnelId_Object=MibTableColumn
tunnelServiceSslTunnelId=_TunnelServiceSslTunnelId_Object((1,3,6,1,4,1,8741,8,1,5,5,1,1),_TunnelServiceSslTunnelId_Type())
tunnelServiceSslTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceSslTunnelId.setStatus(_A)
_TunnelServiceSslTunnelUser_Type=InternationalDisplayString
_TunnelServiceSslTunnelUser_Object=MibTableColumn
tunnelServiceSslTunnelUser=_TunnelServiceSslTunnelUser_Object((1,3,6,1,4,1,8741,8,1,5,5,1,2),_TunnelServiceSslTunnelUser_Type())
tunnelServiceSslTunnelUser.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceSslTunnelUser.setStatus(_A)
_TunnelServiceSslTunnelVIP_Type=InternationalDisplayString
_TunnelServiceSslTunnelVIP_Object=MibTableColumn
tunnelServiceSslTunnelVIP=_TunnelServiceSslTunnelVIP_Object((1,3,6,1,4,1,8741,8,1,5,5,1,3),_TunnelServiceSslTunnelVIP_Type())
tunnelServiceSslTunnelVIP.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceSslTunnelVIP.setStatus(_A)
_NumOfTunnelServiceFlowsPerTunnel_Type=Integer32
_NumOfTunnelServiceFlowsPerTunnel_Object=MibTableColumn
numOfTunnelServiceFlowsPerTunnel=_NumOfTunnelServiceFlowsPerTunnel_Object((1,3,6,1,4,1,8741,8,1,5,5,1,4),_NumOfTunnelServiceFlowsPerTunnel_Type())
numOfTunnelServiceFlowsPerTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:numOfTunnelServiceFlowsPerTunnel.setStatus(_A)
_TunnelServiceSslTunnelUpTime_Type=Integer32
_TunnelServiceSslTunnelUpTime_Object=MibTableColumn
tunnelServiceSslTunnelUpTime=_TunnelServiceSslTunnelUpTime_Object((1,3,6,1,4,1,8741,8,1,5,5,1,5),_TunnelServiceSslTunnelUpTime_Type())
tunnelServiceSslTunnelUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tunnelServiceSslTunnelUpTime.setStatus(_A)
tunnelServiceclientAddrPoolUtilizationWarning=NotificationType((1,3,6,1,4,1,8741,8,1,5,100))
if mibBuilder.loadTexts:tunnelServiceclientAddrPoolUtilizationWarning.setStatus(_A)
tunnelServerStateChange=NotificationType((1,3,6,1,4,1,8741,8,1,5,101))
if mibBuilder.loadTexts:tunnelServerStateChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'sonicwallTunnelServer':sonicwallTunnelServer,'tunnelServerState':tunnelServerState,'numOfTunnelServiceClientAddrPool':numOfTunnelServiceClientAddrPool,'tunnelServiceClientAddrPoolRangesTable':tunnelServiceClientAddrPoolRangesTable,'tunnelServiceClientAddrPoolEntry':tunnelServiceClientAddrPoolEntry,_D:tunnelServiceClientAddrPoolId,'tunnelServiceClientAddrPoolUtilization':tunnelServiceClientAddrPoolUtilization,'tunnelServiceStartRangeOfClientAddrPool':tunnelServiceStartRangeOfClientAddrPool,'tunnelServiceEndRangeOfClientAddrPool':tunnelServiceEndRangeOfClientAddrPool,'numberOfTunnelServiceSslTunnels':numberOfTunnelServiceSslTunnels,'tunnelServiceSslTunnelTable':tunnelServiceSslTunnelTable,'tunnelServiceSslTunnelEntry':tunnelServiceSslTunnelEntry,_E:tunnelServiceSslTunnelId,'tunnelServiceSslTunnelUser':tunnelServiceSslTunnelUser,'tunnelServiceSslTunnelVIP':tunnelServiceSslTunnelVIP,'numOfTunnelServiceFlowsPerTunnel':numOfTunnelServiceFlowsPerTunnel,'tunnelServiceSslTunnelUpTime':tunnelServiceSslTunnelUpTime,'tunnelServiceclientAddrPoolUtilizationWarning':tunnelServiceclientAddrPoolUtilizationWarning,'tunnelServerStateChange':tunnelServerStateChange})