_G='read-write'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ethernetOamRmtLbConfig,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamRmtLbConfig')
_EthernetOamRmtLbCfgTable_Object=MibTable
ethernetOamRmtLbCfgTable=_EthernetOamRmtLbCfgTable_Object((1,3,6,1,4,1,11863,6,60,1,4,1))
if mibBuilder.loadTexts:ethernetOamRmtLbCfgTable.setStatus(_A)
_EthernetOamRmtLbCfgEntry_Object=MibTableRow
ethernetOamRmtLbCfgEntry=_EthernetOamRmtLbCfgEntry_Object((1,3,6,1,4,1,11863,6,60,1,4,1,1))
ethernetOamRmtLbCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ethernetOamRmtLbCfgEntry.setStatus(_A)
_EthernetOamRmtLbCfgPort_Type=DisplayString
_EthernetOamRmtLbCfgPort_Object=MibTableColumn
ethernetOamRmtLbCfgPort=_EthernetOamRmtLbCfgPort_Object((1,3,6,1,4,1,11863,6,60,1,4,1,1,1),_EthernetOamRmtLbCfgPort_Type())
ethernetOamRmtLbCfgPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ethernetOamRmtLbCfgPort.setStatus(_A)
class _EthernetOamRmtLbCfgReceivedRemoteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ignore',0),('process',1)))
_EthernetOamRmtLbCfgReceivedRemoteLoopback_Type.__name__=_B
_EthernetOamRmtLbCfgReceivedRemoteLoopback_Object=MibTableColumn
ethernetOamRmtLbCfgReceivedRemoteLoopback=_EthernetOamRmtLbCfgReceivedRemoteLoopback_Object((1,3,6,1,4,1,11863,6,60,1,4,1,1,2),_EthernetOamRmtLbCfgReceivedRemoteLoopback_Type())
ethernetOamRmtLbCfgReceivedRemoteLoopback.setMaxAccess(_G)
if mibBuilder.loadTexts:ethernetOamRmtLbCfgReceivedRemoteLoopback.setStatus(_A)
class _EthernetOamRmtLbCfgRemoteLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('stop',0),('start',1),('unchanged',2)))
_EthernetOamRmtLbCfgRemoteLoopback_Type.__name__=_B
_EthernetOamRmtLbCfgRemoteLoopback_Object=MibTableColumn
ethernetOamRmtLbCfgRemoteLoopback=_EthernetOamRmtLbCfgRemoteLoopback_Object((1,3,6,1,4,1,11863,6,60,1,4,1,1,3),_EthernetOamRmtLbCfgRemoteLoopback_Type())
ethernetOamRmtLbCfgRemoteLoopback.setMaxAccess(_G)
if mibBuilder.loadTexts:ethernetOamRmtLbCfgRemoteLoopback.setStatus(_A)
class _EthernetOamRmtLbCfgLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EthernetOamRmtLbCfgLAG_Type.__name__=_C
_EthernetOamRmtLbCfgLAG_Object=MibTableColumn
ethernetOamRmtLbCfgLAG=_EthernetOamRmtLbCfgLAG_Object((1,3,6,1,4,1,11863,6,60,1,4,1,1,4),_EthernetOamRmtLbCfgLAG_Type())
ethernetOamRmtLbCfgLAG.setMaxAccess(_F)
if mibBuilder.loadTexts:ethernetOamRmtLbCfgLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ETHERNETOAMRMTLBCFG-MIB',**{'ethernetOamRmtLbCfgTable':ethernetOamRmtLbCfgTable,'ethernetOamRmtLbCfgEntry':ethernetOamRmtLbCfgEntry,'ethernetOamRmtLbCfgPort':ethernetOamRmtLbCfgPort,'ethernetOamRmtLbCfgReceivedRemoteLoopback':ethernetOamRmtLbCfgReceivedRemoteLoopback,'ethernetOamRmtLbCfgRemoteLoopback':ethernetOamRmtLbCfgRemoteLoopback,'ethernetOamRmtLbCfgLAG':ethernetOamRmtLbCfgLAG})