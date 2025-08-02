_E='vpnTunnelTableIndex'
_D='COMPAT-MIB'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Compatible_ObjectIdentity=ObjectIdentity
compatible=_Compatible_ObjectIdentity((1,3,6,1,4,1,255))
_CompatVars_ObjectIdentity=ObjectIdentity
compatVars=_CompatVars_ObjectIdentity((1,3,6,1,4,1,255,1))
_ProcessorUtilizationPercentage_Type=Gauge32
_ProcessorUtilizationPercentage_Object=MibScalar
processorUtilizationPercentage=_ProcessorUtilizationPercentage_Object((1,3,6,1,4,1,255,1,1),_ProcessorUtilizationPercentage_Type())
processorUtilizationPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:processorUtilizationPercentage.setStatus(_A)
_CompatVPN_ObjectIdentity=ObjectIdentity
compatVPN=_CompatVPN_ObjectIdentity((1,3,6,1,4,1,255,2))
_VpnLoginTable_ObjectIdentity=ObjectIdentity
vpnLoginTable=_VpnLoginTable_ObjectIdentity((1,3,6,1,4,1,255,2,1))
_FailedLogins_Type=Counter32
_FailedLogins_Object=MibScalar
failedLogins=_FailedLogins_Object((1,3,6,1,4,1,255,2,1,1),_FailedLogins_Type())
failedLogins.setMaxAccess(_B)
if mibBuilder.loadTexts:failedLogins.setStatus(_A)
_FailedSecurID_Type=Counter32
_FailedSecurID_Object=MibScalar
failedSecurID=_FailedSecurID_Object((1,3,6,1,4,1,255,2,1,2),_FailedSecurID_Type())
failedSecurID.setMaxAccess(_B)
if mibBuilder.loadTexts:failedSecurID.setStatus(_A)
_FailedRadiusAuth_Type=Counter32
_FailedRadiusAuth_Object=MibScalar
failedRadiusAuth=_FailedRadiusAuth_Object((1,3,6,1,4,1,255,2,1,3),_FailedRadiusAuth_Type())
failedRadiusAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:failedRadiusAuth.setStatus(_A)
_VPNTunnelTable_ObjectIdentity=ObjectIdentity
vPNTunnelTable=_VPNTunnelTable_ObjectIdentity((1,3,6,1,4,1,255,2,2))
_VpnTunnelTable_Object=MibTable
vpnTunnelTable=_VpnTunnelTable_Object((1,3,6,1,4,1,255,2,2,1))
if mibBuilder.loadTexts:vpnTunnelTable.setStatus(_A)
_VpnTunnelTableEntry_Object=MibTableRow
vpnTunnelTableEntry=_VpnTunnelTableEntry_Object((1,3,6,1,4,1,255,2,2,1,1))
vpnTunnelTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:vpnTunnelTableEntry.setStatus(_A)
_VpnTunnelTableIndex_Type=Integer32
_VpnTunnelTableIndex_Object=MibTableColumn
vpnTunnelTableIndex=_VpnTunnelTableIndex_Object((1,3,6,1,4,1,255,2,2,1,1,1),_VpnTunnelTableIndex_Type())
vpnTunnelTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableIndex.setStatus(_A)
class _VpnTunnelTableUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VpnTunnelTableUserName_Type.__name__=_C
_VpnTunnelTableUserName_Object=MibTableColumn
vpnTunnelTableUserName=_VpnTunnelTableUserName_Object((1,3,6,1,4,1,255,2,2,1,1,2),_VpnTunnelTableUserName_Type())
vpnTunnelTableUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableUserName.setStatus(_A)
class _VpnTunnelTableGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VpnTunnelTableGroupName_Type.__name__=_C
_VpnTunnelTableGroupName_Object=MibTableColumn
vpnTunnelTableGroupName=_VpnTunnelTableGroupName_Object((1,3,6,1,4,1,255,2,2,1,1,3),_VpnTunnelTableGroupName_Type())
vpnTunnelTableGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableGroupName.setStatus(_A)
_VpnTunnelTableIpAddress_Type=IpAddress
_VpnTunnelTableIpAddress_Object=MibTableColumn
vpnTunnelTableIpAddress=_VpnTunnelTableIpAddress_Object((1,3,6,1,4,1,255,2,2,1,1,4),_VpnTunnelTableIpAddress_Type())
vpnTunnelTableIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableIpAddress.setStatus(_A)
_VpnTunnelTableAssignedIpAddress_Type=IpAddress
_VpnTunnelTableAssignedIpAddress_Object=MibTableColumn
vpnTunnelTableAssignedIpAddress=_VpnTunnelTableAssignedIpAddress_Object((1,3,6,1,4,1,255,2,2,1,1,5),_VpnTunnelTableAssignedIpAddress_Type())
vpnTunnelTableAssignedIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableAssignedIpAddress.setStatus(_A)
_VpnTunnelTableIpBytesRcvd_Type=Counter32
_VpnTunnelTableIpBytesRcvd_Object=MibTableColumn
vpnTunnelTableIpBytesRcvd=_VpnTunnelTableIpBytesRcvd_Object((1,3,6,1,4,1,255,2,2,1,1,6),_VpnTunnelTableIpBytesRcvd_Type())
vpnTunnelTableIpBytesRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableIpBytesRcvd.setStatus(_A)
_VpnTunnelTableIpBytesSent_Type=Counter32
_VpnTunnelTableIpBytesSent_Object=MibTableColumn
vpnTunnelTableIpBytesSent=_VpnTunnelTableIpBytesSent_Object((1,3,6,1,4,1,255,2,2,1,1,7),_VpnTunnelTableIpBytesSent_Type())
vpnTunnelTableIpBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableIpBytesSent.setStatus(_A)
_VpnTunnelTableIpxBytesRcvd_Type=Counter32
_VpnTunnelTableIpxBytesRcvd_Object=MibTableColumn
vpnTunnelTableIpxBytesRcvd=_VpnTunnelTableIpxBytesRcvd_Object((1,3,6,1,4,1,255,2,2,1,1,8),_VpnTunnelTableIpxBytesRcvd_Type())
vpnTunnelTableIpxBytesRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableIpxBytesRcvd.setStatus(_A)
_VpnTunnelTableIpxBytesSent_Type=Counter32
_VpnTunnelTableIpxBytesSent_Object=MibTableColumn
vpnTunnelTableIpxBytesSent=_VpnTunnelTableIpxBytesSent_Object((1,3,6,1,4,1,255,2,2,1,1,9),_VpnTunnelTableIpxBytesSent_Type())
vpnTunnelTableIpxBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableIpxBytesSent.setStatus(_A)
_VpnTunnelTableAppletalkBytesRcvd_Type=Counter32
_VpnTunnelTableAppletalkBytesRcvd_Object=MibTableColumn
vpnTunnelTableAppletalkBytesRcvd=_VpnTunnelTableAppletalkBytesRcvd_Object((1,3,6,1,4,1,255,2,2,1,1,10),_VpnTunnelTableAppletalkBytesRcvd_Type())
vpnTunnelTableAppletalkBytesRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableAppletalkBytesRcvd.setStatus(_A)
_VpnTunnelTableAppletalkBytesSent_Type=Counter32
_VpnTunnelTableAppletalkBytesSent_Object=MibTableColumn
vpnTunnelTableAppletalkBytesSent=_VpnTunnelTableAppletalkBytesSent_Object((1,3,6,1,4,1,255,2,2,1,1,11),_VpnTunnelTableAppletalkBytesSent_Type())
vpnTunnelTableAppletalkBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableAppletalkBytesSent.setStatus(_A)
_VpnTunnelTableUptime_Type=TimeTicks
_VpnTunnelTableUptime_Object=MibTableColumn
vpnTunnelTableUptime=_VpnTunnelTableUptime_Object((1,3,6,1,4,1,255,2,2,1,1,12),_VpnTunnelTableUptime_Type())
vpnTunnelTableUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableUptime.setStatus(_A)
_VpnTunnelTableLatency_Type=Integer32
_VpnTunnelTableLatency_Object=MibTableColumn
vpnTunnelTableLatency=_VpnTunnelTableLatency_Object((1,3,6,1,4,1,255,2,2,1,1,13),_VpnTunnelTableLatency_Type())
vpnTunnelTableLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableLatency.setStatus(_A)
_VpnTunnelTableBandwidthOut_Type=Integer32
_VpnTunnelTableBandwidthOut_Object=MibTableColumn
vpnTunnelTableBandwidthOut=_VpnTunnelTableBandwidthOut_Object((1,3,6,1,4,1,255,2,2,1,1,14),_VpnTunnelTableBandwidthOut_Type())
vpnTunnelTableBandwidthOut.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableBandwidthOut.setStatus(_A)
_VpnTunnelTableBandwidthReturn_Type=Integer32
_VpnTunnelTableBandwidthReturn_Object=MibTableColumn
vpnTunnelTableBandwidthReturn=_VpnTunnelTableBandwidthReturn_Object((1,3,6,1,4,1,255,2,2,1,1,15),_VpnTunnelTableBandwidthReturn_Type())
vpnTunnelTableBandwidthReturn.setMaxAccess(_B)
if mibBuilder.loadTexts:vpnTunnelTableBandwidthReturn.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_C:DisplayString,'compatible':compatible,'compatVars':compatVars,'processorUtilizationPercentage':processorUtilizationPercentage,'compatVPN':compatVPN,'vpnLoginTable':vpnLoginTable,'failedLogins':failedLogins,'failedSecurID':failedSecurID,'failedRadiusAuth':failedRadiusAuth,'vPNTunnelTable':vPNTunnelTable,'vpnTunnelTable':vpnTunnelTable,'vpnTunnelTableEntry':vpnTunnelTableEntry,_E:vpnTunnelTableIndex,'vpnTunnelTableUserName':vpnTunnelTableUserName,'vpnTunnelTableGroupName':vpnTunnelTableGroupName,'vpnTunnelTableIpAddress':vpnTunnelTableIpAddress,'vpnTunnelTableAssignedIpAddress':vpnTunnelTableAssignedIpAddress,'vpnTunnelTableIpBytesRcvd':vpnTunnelTableIpBytesRcvd,'vpnTunnelTableIpBytesSent':vpnTunnelTableIpBytesSent,'vpnTunnelTableIpxBytesRcvd':vpnTunnelTableIpxBytesRcvd,'vpnTunnelTableIpxBytesSent':vpnTunnelTableIpxBytesSent,'vpnTunnelTableAppletalkBytesRcvd':vpnTunnelTableAppletalkBytesRcvd,'vpnTunnelTableAppletalkBytesSent':vpnTunnelTableAppletalkBytesSent,'vpnTunnelTableUptime':vpnTunnelTableUptime,'vpnTunnelTableLatency':vpnTunnelTableLatency,'vpnTunnelTableBandwidthOut':vpnTunnelTableBandwidthOut,'vpnTunnelTableBandwidthReturn':vpnTunnelTableBandwidthReturn})