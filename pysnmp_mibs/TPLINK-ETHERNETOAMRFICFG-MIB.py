_I='read-write'
_H='enable'
_G='disable'
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
ethernetOamRfiConfig,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamRfiConfig')
_EthernetOamRfiCfgTable_Object=MibTable
ethernetOamRfiCfgTable=_EthernetOamRfiCfgTable_Object((1,3,6,1,4,1,11863,6,60,1,3,1))
if mibBuilder.loadTexts:ethernetOamRfiCfgTable.setStatus(_A)
_EthernetOamRfiCfgEntry_Object=MibTableRow
ethernetOamRfiCfgEntry=_EthernetOamRfiCfgEntry_Object((1,3,6,1,4,1,11863,6,60,1,3,1,1))
ethernetOamRfiCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ethernetOamRfiCfgEntry.setStatus(_A)
_EthernetOamRfiCfgPort_Type=DisplayString
_EthernetOamRfiCfgPort_Object=MibTableColumn
ethernetOamRfiCfgPort=_EthernetOamRfiCfgPort_Object((1,3,6,1,4,1,11863,6,60,1,3,1,1,1),_EthernetOamRfiCfgPort_Type())
ethernetOamRfiCfgPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ethernetOamRfiCfgPort.setStatus(_A)
class _EthernetOamRfiCfgDyingGaspNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EthernetOamRfiCfgDyingGaspNotify_Type.__name__=_B
_EthernetOamRfiCfgDyingGaspNotify_Object=MibTableColumn
ethernetOamRfiCfgDyingGaspNotify=_EthernetOamRfiCfgDyingGaspNotify_Object((1,3,6,1,4,1,11863,6,60,1,3,1,1,2),_EthernetOamRfiCfgDyingGaspNotify_Type())
ethernetOamRfiCfgDyingGaspNotify.setMaxAccess(_I)
if mibBuilder.loadTexts:ethernetOamRfiCfgDyingGaspNotify.setStatus(_A)
class _EthernetOamRfiCfgCriticalEventNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_EthernetOamRfiCfgCriticalEventNotify_Type.__name__=_B
_EthernetOamRfiCfgCriticalEventNotify_Object=MibTableColumn
ethernetOamRfiCfgCriticalEventNotify=_EthernetOamRfiCfgCriticalEventNotify_Object((1,3,6,1,4,1,11863,6,60,1,3,1,1,3),_EthernetOamRfiCfgCriticalEventNotify_Type())
ethernetOamRfiCfgCriticalEventNotify.setMaxAccess(_I)
if mibBuilder.loadTexts:ethernetOamRfiCfgCriticalEventNotify.setStatus(_A)
class _EthernetOamRfiCfgLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EthernetOamRfiCfgLAG_Type.__name__=_C
_EthernetOamRfiCfgLAG_Object=MibTableColumn
ethernetOamRfiCfgLAG=_EthernetOamRfiCfgLAG_Object((1,3,6,1,4,1,11863,6,60,1,3,1,1,4),_EthernetOamRfiCfgLAG_Type())
ethernetOamRfiCfgLAG.setMaxAccess(_F)
if mibBuilder.loadTexts:ethernetOamRfiCfgLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ETHERNETOAMRFICFG-MIB',**{'ethernetOamRfiCfgTable':ethernetOamRfiCfgTable,'ethernetOamRfiCfgEntry':ethernetOamRfiCfgEntry,'ethernetOamRfiCfgPort':ethernetOamRfiCfgPort,'ethernetOamRfiCfgDyingGaspNotify':ethernetOamRfiCfgDyingGaspNotify,'ethernetOamRfiCfgCriticalEventNotify':ethernetOamRfiCfgCriticalEventNotify,'ethernetOamRfiCfgLAG':ethernetOamRfiCfgLAG})