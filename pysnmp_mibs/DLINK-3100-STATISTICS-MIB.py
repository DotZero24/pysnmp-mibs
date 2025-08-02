_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlStatistics=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,141))
if mibBuilder.loadTexts:rlStatistics.setRevisions(('2007-11-18 00:00',))
_RlStatisticsPacketTable_Object=MibTable
rlStatisticsPacketTable=_RlStatisticsPacketTable_Object((1,3,6,1,4,1,171,10,94,89,89,141,1))
if mibBuilder.loadTexts:rlStatisticsPacketTable.setStatus(_A)
_RlStatisticsPacketEntry_Object=MibTableRow
rlStatisticsPacketEntry=_RlStatisticsPacketEntry_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1))
rlStatisticsPacketEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rlStatisticsPacketEntry.setStatus(_A)
_RlStatisticsPacket64Octets_Type=Counter32
_RlStatisticsPacket64Octets_Object=MibTableColumn
rlStatisticsPacket64Octets=_RlStatisticsPacket64Octets_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,1),_RlStatisticsPacket64Octets_Type())
rlStatisticsPacket64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacket64Octets.setStatus(_A)
_RlStatisticsPacket65to127Octets_Type=Counter32
_RlStatisticsPacket65to127Octets_Object=MibTableColumn
rlStatisticsPacket65to127Octets=_RlStatisticsPacket65to127Octets_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,2),_RlStatisticsPacket65to127Octets_Type())
rlStatisticsPacket65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacket65to127Octets.setStatus(_A)
_RlStatisticsPacket128to255Octets_Type=Counter32
_RlStatisticsPacket128to255Octets_Object=MibTableColumn
rlStatisticsPacket128to255Octets=_RlStatisticsPacket128to255Octets_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,3),_RlStatisticsPacket128to255Octets_Type())
rlStatisticsPacket128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacket128to255Octets.setStatus(_A)
_RlStatisticsPacket256to511Octets_Type=Counter32
_RlStatisticsPacket256to511Octets_Object=MibTableColumn
rlStatisticsPacket256to511Octets=_RlStatisticsPacket256to511Octets_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,4),_RlStatisticsPacket256to511Octets_Type())
rlStatisticsPacket256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacket256to511Octets.setStatus(_A)
_RlStatisticsPacket512to1023Octets_Type=Counter32
_RlStatisticsPacket512to1023Octets_Object=MibTableColumn
rlStatisticsPacket512to1023Octets=_RlStatisticsPacket512to1023Octets_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,5),_RlStatisticsPacket512to1023Octets_Type())
rlStatisticsPacket512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacket512to1023Octets.setStatus(_A)
_RlStatisticsPacket1024to1518Octets_Type=Counter32
_RlStatisticsPacket1024to1518Octets_Object=MibTableColumn
rlStatisticsPacket1024to1518Octets=_RlStatisticsPacket1024to1518Octets_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,6),_RlStatisticsPacket1024to1518Octets_Type())
rlStatisticsPacket1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacket1024to1518Octets.setStatus(_A)
_RlStatisticsPacketOversizePkts_Type=Counter32
_RlStatisticsPacketOversizePkts_Object=MibTableColumn
rlStatisticsPacketOversizePkts=_RlStatisticsPacketOversizePkts_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,7),_RlStatisticsPacketOversizePkts_Type())
rlStatisticsPacketOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketOversizePkts.setStatus(_A)
_RlStatisticsPacketUnicastRx_Type=Counter32
_RlStatisticsPacketUnicastRx_Object=MibTableColumn
rlStatisticsPacketUnicastRx=_RlStatisticsPacketUnicastRx_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,8),_RlStatisticsPacketUnicastRx_Type())
rlStatisticsPacketUnicastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketUnicastRx.setStatus(_A)
_RlStatisticsPacketMulticastRx_Type=Counter32
_RlStatisticsPacketMulticastRx_Object=MibTableColumn
rlStatisticsPacketMulticastRx=_RlStatisticsPacketMulticastRx_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,9),_RlStatisticsPacketMulticastRx_Type())
rlStatisticsPacketMulticastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketMulticastRx.setStatus(_A)
_RlStatisticsPacketBroadcastRx_Type=Counter32
_RlStatisticsPacketBroadcastRx_Object=MibTableColumn
rlStatisticsPacketBroadcastRx=_RlStatisticsPacketBroadcastRx_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,10),_RlStatisticsPacketBroadcastRx_Type())
rlStatisticsPacketBroadcastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketBroadcastRx.setStatus(_A)
_RlStatisticsPacketRxBytes_Type=Counter32
_RlStatisticsPacketRxBytes_Object=MibTableColumn
rlStatisticsPacketRxBytes=_RlStatisticsPacketRxBytes_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,11),_RlStatisticsPacketRxBytes_Type())
rlStatisticsPacketRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketRxBytes.setStatus(_A)
_RlStatisticsPacketRxFrames_Type=Counter32
_RlStatisticsPacketRxFrames_Object=MibTableColumn
rlStatisticsPacketRxFrames=_RlStatisticsPacketRxFrames_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,12),_RlStatisticsPacketRxFrames_Type())
rlStatisticsPacketRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketRxFrames.setStatus(_A)
_RlStatisticsPacketTxBytes_Type=Counter32
_RlStatisticsPacketTxBytes_Object=MibTableColumn
rlStatisticsPacketTxBytes=_RlStatisticsPacketTxBytes_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,13),_RlStatisticsPacketTxBytes_Type())
rlStatisticsPacketTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketTxBytes.setStatus(_A)
_RlStatisticsPacketTxFrames_Type=Counter32
_RlStatisticsPacketTxFrames_Object=MibTableColumn
rlStatisticsPacketTxFrames=_RlStatisticsPacketTxFrames_Object((1,3,6,1,4,1,171,10,94,89,89,141,1,1,14),_RlStatisticsPacketTxFrames_Type())
rlStatisticsPacketTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPacketTxFrames.setStatus(_A)
_RlStatisticsPortTable_Object=MibTable
rlStatisticsPortTable=_RlStatisticsPortTable_Object((1,3,6,1,4,1,171,10,94,89,89,141,2))
if mibBuilder.loadTexts:rlStatisticsPortTable.setStatus(_A)
_RlStatisticsPortEntry_Object=MibTableRow
rlStatisticsPortEntry=_RlStatisticsPortEntry_Object((1,3,6,1,4,1,171,10,94,89,89,141,2,1))
rlStatisticsPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rlStatisticsPortEntry.setStatus(_A)
_RlStatisticsPortRx_Type=Counter32
_RlStatisticsPortRx_Object=MibTableColumn
rlStatisticsPortRx=_RlStatisticsPortRx_Object((1,3,6,1,4,1,171,10,94,89,89,141,2,1,1),_RlStatisticsPortRx_Type())
rlStatisticsPortRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPortRx.setStatus(_A)
_RlStatisticsPortTx_Type=Counter32
_RlStatisticsPortTx_Object=MibTableColumn
rlStatisticsPortTx=_RlStatisticsPortTx_Object((1,3,6,1,4,1,171,10,94,89,89,141,2,1,2),_RlStatisticsPortTx_Type())
rlStatisticsPortTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPortTx.setStatus(_A)
class _RlStatisticsPortUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_RlStatisticsPortUtilization_Type.__name__=_E
_RlStatisticsPortUtilization_Object=MibTableColumn
rlStatisticsPortUtilization=_RlStatisticsPortUtilization_Object((1,3,6,1,4,1,171,10,94,89,89,141,2,1,3),_RlStatisticsPortUtilization_Type())
rlStatisticsPortUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:rlStatisticsPortUtilization.setStatus(_A)
mibBuilder.exportSymbols('DLINK-3100-STATISTICS-MIB',**{'rlStatistics':rlStatistics,'rlStatisticsPacketTable':rlStatisticsPacketTable,'rlStatisticsPacketEntry':rlStatisticsPacketEntry,'rlStatisticsPacket64Octets':rlStatisticsPacket64Octets,'rlStatisticsPacket65to127Octets':rlStatisticsPacket65to127Octets,'rlStatisticsPacket128to255Octets':rlStatisticsPacket128to255Octets,'rlStatisticsPacket256to511Octets':rlStatisticsPacket256to511Octets,'rlStatisticsPacket512to1023Octets':rlStatisticsPacket512to1023Octets,'rlStatisticsPacket1024to1518Octets':rlStatisticsPacket1024to1518Octets,'rlStatisticsPacketOversizePkts':rlStatisticsPacketOversizePkts,'rlStatisticsPacketUnicastRx':rlStatisticsPacketUnicastRx,'rlStatisticsPacketMulticastRx':rlStatisticsPacketMulticastRx,'rlStatisticsPacketBroadcastRx':rlStatisticsPacketBroadcastRx,'rlStatisticsPacketRxBytes':rlStatisticsPacketRxBytes,'rlStatisticsPacketRxFrames':rlStatisticsPacketRxFrames,'rlStatisticsPacketTxBytes':rlStatisticsPacketTxBytes,'rlStatisticsPacketTxFrames':rlStatisticsPacketTxFrames,'rlStatisticsPortTable':rlStatisticsPortTable,'rlStatisticsPortEntry':rlStatisticsPortEntry,'rlStatisticsPortRx':rlStatisticsPortRx,'rlStatisticsPortTx':rlStatisticsPortTx,'rlStatisticsPortUtilization':rlStatisticsPortUtilization})