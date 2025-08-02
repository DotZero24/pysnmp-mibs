_E='h3cVpnPeerName'
_D='H3C-VPN-PEER-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVpnPeer=ModuleIdentity((1,3,6,1,4,1,2011,10,2,165))
if mibBuilder.loadTexts:h3cVpnPeer.setRevisions(('2016-03-09 16:00',))
_H3cVpnPeerGroup_ObjectIdentity=ObjectIdentity
h3cVpnPeerGroup=_H3cVpnPeerGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,165,1))
_H3cVpnPeerStat_ObjectIdentity=ObjectIdentity
h3cVpnPeerStat=_H3cVpnPeerStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,165,1,1))
_H3cVpnPeerStatTable_Object=MibTable
h3cVpnPeerStatTable=_H3cVpnPeerStatTable_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1))
if mibBuilder.loadTexts:h3cVpnPeerStatTable.setStatus(_A)
_H3cVpnPeerStatEntry_Object=MibTableRow
h3cVpnPeerStatEntry=_H3cVpnPeerStatEntry_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1,1))
h3cVpnPeerStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cVpnPeerStatEntry.setStatus(_A)
class _H3cVpnPeerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cVpnPeerName_Type.__name__=_C
_H3cVpnPeerName_Object=MibTableColumn
h3cVpnPeerName=_H3cVpnPeerName_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1,1,1),_H3cVpnPeerName_Type())
h3cVpnPeerName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cVpnPeerName.setStatus(_A)
_H3cVpnPeerOutPassPkts_Type=Counter64
_H3cVpnPeerOutPassPkts_Object=MibTableColumn
h3cVpnPeerOutPassPkts=_H3cVpnPeerOutPassPkts_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1,1,2),_H3cVpnPeerOutPassPkts_Type())
h3cVpnPeerOutPassPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVpnPeerOutPassPkts.setStatus(_A)
_H3cVpnPeerOutPassBytes_Type=Counter64
_H3cVpnPeerOutPassBytes_Object=MibTableColumn
h3cVpnPeerOutPassBytes=_H3cVpnPeerOutPassBytes_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1,1,3),_H3cVpnPeerOutPassBytes_Type())
h3cVpnPeerOutPassBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVpnPeerOutPassBytes.setStatus(_A)
_H3cVpnPeerOutDropPkts_Type=Counter64
_H3cVpnPeerOutDropPkts_Object=MibTableColumn
h3cVpnPeerOutDropPkts=_H3cVpnPeerOutDropPkts_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1,1,4),_H3cVpnPeerOutDropPkts_Type())
h3cVpnPeerOutDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVpnPeerOutDropPkts.setStatus(_A)
_H3cVpnPeerOutDropBytes_Type=Counter64
_H3cVpnPeerOutDropBytes_Object=MibTableColumn
h3cVpnPeerOutDropBytes=_H3cVpnPeerOutDropBytes_Object((1,3,6,1,4,1,2011,10,2,165,1,1,1,1,5),_H3cVpnPeerOutDropBytes_Type())
h3cVpnPeerOutDropBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVpnPeerOutDropBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cVpnPeer':h3cVpnPeer,'h3cVpnPeerGroup':h3cVpnPeerGroup,'h3cVpnPeerStat':h3cVpnPeerStat,'h3cVpnPeerStatTable':h3cVpnPeerStatTable,'h3cVpnPeerStatEntry':h3cVpnPeerStatEntry,_E:h3cVpnPeerName,'h3cVpnPeerOutPassPkts':h3cVpnPeerOutPassPkts,'h3cVpnPeerOutPassBytes':h3cVpnPeerOutPassBytes,'h3cVpnPeerOutDropPkts':h3cVpnPeerOutDropPkts,'h3cVpnPeerOutDropBytes':h3cVpnPeerOutDropBytes})