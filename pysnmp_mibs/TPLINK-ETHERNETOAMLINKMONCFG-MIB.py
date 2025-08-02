_I='ethernetOamLinkMonCfgEvent'
_H='TPLINK-ETHERNETOAMLINKMONCFG-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ethernetOamLinkMonConfig,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamLinkMonConfig')
_EthernetOamLinkMonCfgTable_Object=MibTable
ethernetOamLinkMonCfgTable=_EthernetOamLinkMonCfgTable_Object((1,3,6,1,4,1,11863,6,60,1,2,1))
if mibBuilder.loadTexts:ethernetOamLinkMonCfgTable.setStatus(_A)
_EthernetOamLinkMonCfgEntry_Object=MibTableRow
ethernetOamLinkMonCfgEntry=_EthernetOamLinkMonCfgEntry_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1))
ethernetOamLinkMonCfgEntry.setIndexNames((0,_F,_G),(0,_H,_I))
if mibBuilder.loadTexts:ethernetOamLinkMonCfgEntry.setStatus(_A)
_EthernetOamLinkMonCfgPort_Type=DisplayString
_EthernetOamLinkMonCfgPort_Object=MibTableColumn
ethernetOamLinkMonCfgPort=_EthernetOamLinkMonCfgPort_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1,1),_EthernetOamLinkMonCfgPort_Type())
ethernetOamLinkMonCfgPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ethernetOamLinkMonCfgPort.setStatus(_A)
class _EthernetOamLinkMonCfgEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('symbol-period',1),('frame',2),('frame-period',3),('frame-seconds',4)))
_EthernetOamLinkMonCfgEvent_Type.__name__=_B
_EthernetOamLinkMonCfgEvent_Object=MibTableColumn
ethernetOamLinkMonCfgEvent=_EthernetOamLinkMonCfgEvent_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1,2),_EthernetOamLinkMonCfgEvent_Type())
ethernetOamLinkMonCfgEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:ethernetOamLinkMonCfgEvent.setStatus(_A)
_EthernetOamLinkMonCfgThreshold_Type=Unsigned32
_EthernetOamLinkMonCfgThreshold_Object=MibTableColumn
ethernetOamLinkMonCfgThreshold=_EthernetOamLinkMonCfgThreshold_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1,3),_EthernetOamLinkMonCfgThreshold_Type())
ethernetOamLinkMonCfgThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ethernetOamLinkMonCfgThreshold.setStatus(_A)
_EthernetOamLinkMonCfgWindow_Type=Unsigned32
_EthernetOamLinkMonCfgWindow_Object=MibTableColumn
ethernetOamLinkMonCfgWindow=_EthernetOamLinkMonCfgWindow_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1,4),_EthernetOamLinkMonCfgWindow_Type())
ethernetOamLinkMonCfgWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:ethernetOamLinkMonCfgWindow.setStatus(_A)
class _EthernetOamLinkMonCfgNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_EthernetOamLinkMonCfgNotify_Type.__name__=_B
_EthernetOamLinkMonCfgNotify_Object=MibTableColumn
ethernetOamLinkMonCfgNotify=_EthernetOamLinkMonCfgNotify_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1,5),_EthernetOamLinkMonCfgNotify_Type())
ethernetOamLinkMonCfgNotify.setMaxAccess(_D)
if mibBuilder.loadTexts:ethernetOamLinkMonCfgNotify.setStatus(_A)
class _EthernetOamLinkMonCfgLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EthernetOamLinkMonCfgLAG_Type.__name__=_E
_EthernetOamLinkMonCfgLAG_Object=MibTableColumn
ethernetOamLinkMonCfgLAG=_EthernetOamLinkMonCfgLAG_Object((1,3,6,1,4,1,11863,6,60,1,2,1,1,6),_EthernetOamLinkMonCfgLAG_Type())
ethernetOamLinkMonCfgLAG.setMaxAccess(_C)
if mibBuilder.loadTexts:ethernetOamLinkMonCfgLAG.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'ethernetOamLinkMonCfgTable':ethernetOamLinkMonCfgTable,'ethernetOamLinkMonCfgEntry':ethernetOamLinkMonCfgEntry,'ethernetOamLinkMonCfgPort':ethernetOamLinkMonCfgPort,_I:ethernetOamLinkMonCfgEvent,'ethernetOamLinkMonCfgThreshold':ethernetOamLinkMonCfgThreshold,'ethernetOamLinkMonCfgWindow':ethernetOamLinkMonCfgWindow,'ethernetOamLinkMonCfgNotify':ethernetOamLinkMonCfgNotify,'ethernetOamLinkMonCfgLAG':ethernetOamLinkMonCfgLAG})