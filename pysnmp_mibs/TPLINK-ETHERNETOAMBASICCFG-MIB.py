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
ethernetOamBasicConfig,=mibBuilder.importSymbols('TPLINK-ETHERNETOAM-MIB','ethernetOamBasicConfig')
_EthernetOamBasicCfgTable_Object=MibTable
ethernetOamBasicCfgTable=_EthernetOamBasicCfgTable_Object((1,3,6,1,4,1,11863,6,60,1,1,1))
if mibBuilder.loadTexts:ethernetOamBasicCfgTable.setStatus(_A)
_EthernetOamBasicCfgEntry_Object=MibTableRow
ethernetOamBasicCfgEntry=_EthernetOamBasicCfgEntry_Object((1,3,6,1,4,1,11863,6,60,1,1,1,1))
ethernetOamBasicCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ethernetOamBasicCfgEntry.setStatus(_A)
_EthernetOamBasicCfgPort_Type=DisplayString
_EthernetOamBasicCfgPort_Object=MibTableColumn
ethernetOamBasicCfgPort=_EthernetOamBasicCfgPort_Object((1,3,6,1,4,1,11863,6,60,1,1,1,1,1),_EthernetOamBasicCfgPort_Type())
ethernetOamBasicCfgPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ethernetOamBasicCfgPort.setStatus(_A)
class _EthernetOamBasicCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('passive',0),('active',1)))
_EthernetOamBasicCfgMode_Type.__name__=_B
_EthernetOamBasicCfgMode_Object=MibTableColumn
ethernetOamBasicCfgMode=_EthernetOamBasicCfgMode_Object((1,3,6,1,4,1,11863,6,60,1,1,1,1,2),_EthernetOamBasicCfgMode_Type())
ethernetOamBasicCfgMode.setMaxAccess(_G)
if mibBuilder.loadTexts:ethernetOamBasicCfgMode.setStatus(_A)
class _EthernetOamBasicCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_EthernetOamBasicCfgState_Type.__name__=_B
_EthernetOamBasicCfgState_Object=MibTableColumn
ethernetOamBasicCfgState=_EthernetOamBasicCfgState_Object((1,3,6,1,4,1,11863,6,60,1,1,1,1,3),_EthernetOamBasicCfgState_Type())
ethernetOamBasicCfgState.setMaxAccess(_G)
if mibBuilder.loadTexts:ethernetOamBasicCfgState.setStatus(_A)
class _EthernetOamBasicCfgLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_EthernetOamBasicCfgLAG_Type.__name__=_C
_EthernetOamBasicCfgLAG_Object=MibTableColumn
ethernetOamBasicCfgLAG=_EthernetOamBasicCfgLAG_Object((1,3,6,1,4,1,11863,6,60,1,1,1,1,4),_EthernetOamBasicCfgLAG_Type())
ethernetOamBasicCfgLAG.setMaxAccess(_F)
if mibBuilder.loadTexts:ethernetOamBasicCfgLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ETHERNETOAMBASICCFG-MIB',**{'ethernetOamBasicCfgTable':ethernetOamBasicCfgTable,'ethernetOamBasicCfgEntry':ethernetOamBasicCfgEntry,'ethernetOamBasicCfgPort':ethernetOamBasicCfgPort,'ethernetOamBasicCfgMode':ethernetOamBasicCfgMode,'ethernetOamBasicCfgState':ethernetOamBasicCfgState,'ethernetOamBasicCfgLAG':ethernetOamBasicCfgLAG})